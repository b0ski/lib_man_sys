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
cur.execute("INSERT INTO users (name, gender, email) VALUES ('Trevor', 'm', 'traint@gmail.com')")

# Query the database
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:
    for row in rows:
        print(row)

# Close communications with database
cur.close()
conn.close()
