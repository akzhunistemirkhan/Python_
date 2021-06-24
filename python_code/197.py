import psycopg2
conn = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Aray2020", 
  host="localhost")

cur = conn.cursor() 

sql = """
SELECT * FROM participants 
"""
cur.execute(sql)

row = cur.fetchone()
while row is not None:
    print(row)
    row = cur.fetchone()

print(cur.rowcount)

cur.close()
conn.commit()  
