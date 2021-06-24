import psycopg2

conn = psycopg2.connect( 
        "localhost",
        database="postgres",
        user="postgres",
        password="Aray2020"
)

sql = 'select id, user_type, subscription_id from authe_usertype where subscription_id=63'

cursor = conn.cursor()
cursor.execute(sql)
all_rows = cursor.fetchall()
print(all_rows)


# for row in cursor:
#     print(row)

cursor.close()
conn.close()