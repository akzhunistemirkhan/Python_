import psycopg2

conn = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Aray2020", 
  host="localhost")

cur = conn.cursor() 

sql = """
INSERT INTO participants1(name) VALUES (%s) RETURNING name, text
"""

participants_name = 'Anel'
cur.execute(sql, (participants_name,))


inserted_name = cur.fetchone()
print(inserted_name)

cur.close()
conn.close()  

      