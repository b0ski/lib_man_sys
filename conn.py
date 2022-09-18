# https://www.psycopg.org/docs/usage.html
import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="exampledb",
    user="docker",
    password="docker",
    host="0.0.0.0"
)

# Open cursor to perform database operation
cur = conn.cursor()

# Insert data
# cur.execute("INSERT INTO book (title, genre, rating) VALUES ('Fight Club', 'Thriller', 5)")

# Query the database
cur.execute("SELECT * FROM book")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close communications with database
cur.close()
conn.close()
