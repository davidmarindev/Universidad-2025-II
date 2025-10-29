from db import crear_conn

connection = crear_conn()
cursor = connection.cursor()

cursor.execute("SELECT * FROM products")

rows = cursor.fetchall()
for row in rows:
    print(row)
