import sqlite3

conn = sqlite3.connect("../guardianDB.sqlite")
cursor = conn.cursor()

schema = open("../schema.sql")
query = schema.read()
cursor.executescript(query)
