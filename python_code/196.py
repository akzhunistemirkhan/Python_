import psycopg2

conn = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Aray2020", 
  host="localhost")

cur = conn.cursor() 

sql = """
UPDATE participants1 SET text=%s WHERE name=%s  
"""
text = 'My name is Anel'
participants_name = 'Anel'
cur.execute(sql, (text, participants_name,))

print(cur.rowcount)

cur.close()
conn.commit()  

      