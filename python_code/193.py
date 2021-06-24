import psycopg2

conn = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Aray2020", 
  host="localhost")

cur = conn.cursor()
print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)
       
cur.close()
conn.close()
