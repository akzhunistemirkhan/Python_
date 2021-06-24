import psycopg2
conn = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Aray2020", 
  host="localhost")

cur = conn.cursor() 

sql = """
DELETE FROM participants WHERE name=%s
"""
participants_name = 'participants 1'
cur.execute(sql, (participants_name,))

print(cur.rowcount)

cur.close()
conn.commit()  
