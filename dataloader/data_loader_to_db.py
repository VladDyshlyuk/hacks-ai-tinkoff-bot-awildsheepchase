from sentence_transformers import SentenceTransformer
from vector_db import Database
import json
import configparser

# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer("distiluse-base-multilingual-cased-v1")

dbname = ""
dbhost = ""
dbuser = ""
dbpassword = ""
dbport = ""
dimension = '512'
table_name = 'table_name'
db = Database(dbname, dbhost, dbuser, dbpassword, dbport)


def load_dataset(dataset: str, database: Database, model: SentenceTransformer, table_name='vector_table'):
    with open(dataset, encoding="utf-8") as file:
        data = json.load(file)

    contents = []
    urls = []

    for item in data["data"]:
        content = item["title"] + " " + item["description"]
        metadata = item["url"]
        contents.append(content)
        urls.append(metadata)

    embeddings = model.encode(contents)
    for content, embedding, url in zip(contents, embeddings, urls):
        database.add_values(content, embedding, url, table_name=table_name)


filename = "dataset.json"
ds = f"datasets/{filename}"
load_dataset(ds, db, model, table_name=table_name)
