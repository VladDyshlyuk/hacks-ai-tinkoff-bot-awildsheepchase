from pgvector.psycopg import register_vector
import psycopg

class Database:
    
    def __init__(self, dbname, host, user, password, port):
        self.conn = psycopg.connect(dbname=dbname, host=host, user=user, password=password, port=port, autocommit=True)
        self.conn.execute('CREATE EXTENSION IF NOT EXISTS vector')
        register_vector(self.conn)

        
    def create_database(self, dimension='384', table_name='test'): # создает таблицу в базе данных, если она уже существует, то удаляет ее и создает новую
        self.conn.execute(f'DROP TABLE IF EXISTS {table_name}')
        self.conn.execute(f'CREATE TABLE {table_name} (id bigserial PRIMARY KEY, content text, embedding vector({dimension}), urls text)')
        self.conn.execute(f"CREATE INDEX ON {table_name} USING GIN (to_tsvector('russian', content))")

    def add_values(self, content, embedding, urls, table_name='test'): # добавляет значениия в таблицу
        self.conn.execute(f'INSERT INTO {table_name} (content, embedding, urls) VALUES (%s, %s, %s)', (content, embedding, urls))

    def db_search(self, query, model, table_name='test', n=3): # выполняет поиск по таблице по запросу
        embedding = model.encode(query)
        k = 60
        sql = f"""
        WITH semantic_search AS (
            SELECT id, RANK () OVER (ORDER BY embedding <=> %(embedding)s) AS rank
            FROM {table_name}
            ORDER BY embedding <=> %(embedding)s
            LIMIT 20
        ),
        keyword_search AS (
            SELECT id, RANK () OVER (ORDER BY ts_rank_cd(to_tsvector('russian', content), query) DESC)
            FROM {table_name}, plainto_tsquery('russian', %(query)s) query
            WHERE to_tsvector('russian', content) @@ query
            ORDER BY ts_rank_cd(to_tsvector('russian', content), query) DESC
            LIMIT 20
        )
        SELECT
            COALESCE(semantic_search.id, keyword_search.id) AS id,
            COALESCE(1.0 / (%(k)s + semantic_search.rank), 0.0) +
            COALESCE(1.0 / (%(k)s + keyword_search.rank), 0.0) AS score
        FROM semantic_search
        FULL OUTER JOIN keyword_search ON semantic_search.id = keyword_search.id
        ORDER BY score DESC
        LIMIT {n}

        """

        self.results = self.conn.execute(sql, {'query': query, 'embedding': embedding, 'k': k}).fetchall()
        self.answers = []
        self.sources = []


        for i in range(len(self.results)):
            if self.results[i][1] >= 0.0164:
                self.answers.append(self.conn.execute(f'SELECT content FROM {table_name} WHERE id = %(id)s', {'id': self.results[i][0]}).fetchall()[0][0])
                self.sources.append(self.conn.execute(f'SELECT urls FROM {table_name} WHERE id = %(id)s', {'id': self.results[i][0]}).fetchall()[0][0])
            
        return self.answers, self.sources