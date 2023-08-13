# import psycopg2 module to connect to PostgreSQL database
import psycopg2

# Define database info
hostname = 'localhost'
database = 'valuation_tool_db'
username = 'postgres'
pwd = 'Dice123!'
port_id = '5432'

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
    insert_values = ('2', 'audi')

    # Execute insert script to insert values into the table
    cursor.execute(insert_script, insert_values)

    # Commit execution
    conn.commit()
    print('Added to db')

except Exception as error:
        print(error)
        print('Could not connect to db')