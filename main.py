import psycopg2
from psycopg2 import sql

# Database connection parameters
dbname = "sampledb"
user = "user8BV"
password = "ANI3OSDTJsYCUH07"
host = "localhost"  # or the specific host if it's not local

# Connect to your postgres DB
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# Open a cursor to perform database operations
cur = conn.cursor()

# Check if the table exists, and create it if it doesn't
cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s);", ('example-table',))
if not cur.fetchone()[0]:
    cur.execute("CREATE TABLE example_table (id serial PRIMARY KEY, data varchar);")

# Check if there's at least one entry in the table
cur.execute("SELECT COUNT(*) FROM example_table;")
if cur.fetchone()[0] == 0:
    # Insert a row if the table is empty
    cur.execute("INSERT INTO example_table (data) VALUES ('Sample Data');")

# Commit the transaction
conn.commit()

# Retrieve and print all records from the table
cur.execute("SELECT * FROM example_table;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()