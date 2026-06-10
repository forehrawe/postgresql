import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="mydb",
    user="hadi",
    password="1234"
)

cursor = conn.cursor()

cursor.execute('insert into users (name, age) values (%s, %s)', ('reza', 30))
conn.commit()

cursor.execute('select * from users')
rows = cursor.fetchall()
for row in rows:
    print(row)