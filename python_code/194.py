import psycopg2

conn = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="Aray2020", 
  host="localhost")

cur = conn.cursor()  

cur.execute("""
CREATE TABLE participants1 (
    name VARCHAR(255),
    surname VARCHAR(255),
    age INTEGER,
    text TEXT,
    point INTEGER,
    date DATE
);
""")
print("Table created successfully")
cur.close()
conn.commit()  
