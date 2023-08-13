# import psycopg2 module to connect to PostgreSQL database
import psycopg2

# import 'os' to access environment variables.
import os

# Retrieve environment variables using os.environ.get('VARIABLE_NAME')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_port = os.environ.get('DB_PORT')



# Define database info
hostname = db_host
database = db_name
username = db_user
pwd = db_password
port_id = db_port

# Reset connection and cursor
conn = None
cursor = None

# Check connection
try:
    # Connect to database
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    # Open a cursor to perform SQL operationa
    cursor = conn.cursor()

    # Insert data into table
    insert_script = 'INSERT INTO car_make_tbl (make_id, make) VALUES(%s, %s)'
    insert_values = ('4', 'volkswagen')

    # Execute insert script to insert values into the table
    cursor.execute(insert_script, insert_values)

    # Commit execution
    conn.commit()
    print('Added to db')

except Exception as error:
        print(error)
        print('Could not connect to db')