import psycopg2
import time
from psycopg2 import sql

# Database connection parameters
dbname = "sampledb"
user = "user8BV"
password = "ANI3OSDTJsYCUH07"
host = "postgresql.playground.svc.cluster.local"  # or the specific host if it's not local

def connect_to_db(dbname, user, password, host):
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    except Exception as e:
        print(f"The error '{e}' occurred")
    return conn

def check_table_exists(conn, table_name):
    """Check if a table exists in the current database."""
    exists = False
    try:
        # Create a cursor object
        cur = conn.cursor()

        # Check if table exists
        cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s);", (table_name,))
        exists = cur.fetchone()[0]

        # Close the cursor
        cur.close()
    except Exception as e:
        print(f"The error '{e}' occurred")
    
    return exists

# Connect to the database
while True:
    conn = connect_to_db(dbname, user, password, host)


    # Check if table exists
    table_name = "example_table"
    if conn is not None:
        if check_table_exists(conn, table_name):
            print(f"Table {table_name} exists.")
        else:
            print(f"Table {table_name} does not exist.")

    else:
        print("Connection to database failed.")
        exit()

    cur = conn.cursor()

    # Retrieve and print all records from the table
    cur.execute("SELECT * FROM example_table;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    # Close the connection
    conn.close()
    time.sleep(30)