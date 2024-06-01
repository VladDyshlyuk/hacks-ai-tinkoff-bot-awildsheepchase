from vector_db import Database
import configparser

dbname = ""
dbhost = ""
dbuser = ""
dbpassword = ""
dbport = ""
dimension = '512'
table_name = 'table_name'
db = Database(dbname, dbhost, dbuser, dbpassword, dbport)


db.create_database(dimension=dimension, table_name=table_name)

# ВНИМАНИЕ: СОЗДАНИЕ УЖЕ СУЩЕСТВУЮЩЕЙ ТАБЛИЦЫ СОТРЕТ ПРЕДШЕСТУЮЩУЮ
