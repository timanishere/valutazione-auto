# Import flask
from flask import Flask, render_template, request, jsonify

# import psycopg2 module to connect to PostgreSQL database
import psycopg2

# import psycopg2.extras module to return data as a tuple
import psycopg2.extras

# import 'os' to access environment variables.
import os

import locale

# Set the locale to Italian
locale.setlocale(locale.LC_ALL, 'it_IT')

# Create instance of web app
app = Flask(__name__)

# Check connection to the DB
try:
    # Retrieve environment variables using os.environ.get('VARIABLE_NAME')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_port = os.environ.get('DB_PORT')

    # Connect to database
    conn = psycopg2.connect(
        host = db_host,
        dbname = db_name,
        user = db_user,
        password = db_password,
        port = db_port
    )   

    print('Connected to db')
except Exception as error:
      print(error)
      print('Could not connect to db')

# Open a cursor to perform SQL operationan and return data as a dictionary
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Query database to get list car makes
cursor.execute('SELECT * FROM car_make_list_tbl')

# Store car make list
car_make_list_arr = cursor.fetchall()

# Query database to get list years
cursor.execute('SELECT * FROM car_year_tbl ORDER BY year DESC')

# Store car make list
car_year_list_arr = cursor.fetchall()

# Query database to get list of colours
cursor.execute('SELECT colour FROM car_colour_tbl ORDER BY colour')

# Store car make list
car_colour_list_arr = cursor.fetchall()

# Query database to get list of gears
cursor.execute('SELECT * FROM car_gear_tbl')

# Store car make list
car_gear_list_arr = cursor.fetchall()

# Query database to get list of fuel type
cursor.execute('SELECT * FROM car_fuel_type_tbl')

# Store fuel type list
car_fuel_type_list_arr = cursor.fetchall()

# Define route
@app.route('/valutazione-auto')

# Define webpage
def index():
    return render_template('index.html', car_make_list_arr=car_make_list_arr, car_year_list_arr=car_year_list_arr, car_colour_list_arr=car_colour_list_arr, car_gear_list_arr=car_gear_list_arr, car_fuel_type_list_arr=car_fuel_type_list_arr)

# Define route called process
@app.route('/process', methods = ['POST'])

# Define function for the process route
def process():

    # Fetch json data sent from javascript
    data = request.get_json

    # Store the JSON object
    result = data('car_make')

    # Get car make value from drop down
    car_make_val = result['car_make']

    # Query car_make_list_tbl to get the car make data
    cursor.execute(f'''
        SELECT * FROM car_make_list_tbl WHERE car_make = '{car_make_val}'
    ''')

    # Store query results
    query_results_arr = cursor.fetchall()

    # Get value from 'make_and_model_table_name' column
    make_and_model_table_name = query_results_arr[0][3]

    # Query the cars make_and_model_tbl to return list of models
    cursor.execute(f'''
        SELECT model FROM {make_and_model_table_name} ORDER BY model
    ''')

    car_model_list = cursor.fetchall()

    return car_model_list


    
# Create route for getting data
@app.route('/valutazione-auto/risultato', methods = ['POST'])

# Create insert function
def results():
    # Check if request is POST
    if request.method == 'POST':

        # Get form values
        form_value_make = request.form['make']
        form_value_model = request.form['model']
        form_value_year = request.form['year']
        form_value_colour = request.form['colour']
        form_value_gear = request.form['gear']
        form_value_fuelType = request.form['fuelType']
        form_value_km = request.form['km']
        
        form_value_km_int = int(form_value_km)

        # Calculated total number of characters for km
        km_num_of_chars = len(form_value_km)

        # Subtract 2. This will be used to loop number of zeros to add
        num_of_zeros = km_num_of_chars - 2

        # Set the beginning of the number to add zeros
        km_range_y = '5'

        km_range_x = ''

        for x in range(num_of_zeros):
            
            km_range_x = km_range_x + '0'

        km_range_increment = km_range_y + km_range_x

        km_range_increment = int(km_range_increment)

        km_range_end = km_range_increment + form_value_km_int

        km_range_end = km_range_end * 1

        print(km_range_end)

        # Query car_make_list_tbl to get the car make data
        cursor.execute(f'''
            SELECT * FROM car_make_list_tbl WHERE car_make = '{form_value_make}'
        ''')

        # Store query results
        car_data_arr = cursor.fetchall()

        # Get value from 'make_and_model_table_name' column
        make_and_model_table_name = car_data_arr[0][3]

        # Get value from 'price_table_name' column
        price_table_name = car_data_arr[0][2]

        # Query database to get average price
        cursor.execute(f'''
            WITH car_prices AS (
                SELECT
                    cm.make,
                    cm.model,
                    cy.year,
                    cc.colour,
                    cg.gear,
                    ft.fuel_type,
                    cp.km,
                    cp.price
                FROM {price_table_name} AS cp
                JOIN {make_and_model_table_name} AS cm
                    ON cp.make_and_model_id = cm.make_and_model_id
                JOIN car_colour_tbl AS cc
                    ON cp.colour_id = cc.colour_id
                JOIN car_fuel_type_tbl AS ft
                    ON cp.fuel_type_id = ft.fuel_type_id
                JOIN car_gear_tbl AS cg
                    ON cp.gear_id = cg.gear_id
                JOIN car_year_tbl AS cy
                    ON cp.year_id = cy.year_id
                WHERE 
                    make = '{form_value_make}' AND
                    model = '{form_value_model}' AND
                    colour = '{form_value_colour}' AND
                    fuel_type = '{form_value_fuelType}' AND
                    year = {form_value_year} AND 
                    gear = '{form_value_gear}' AND
                    km >= {form_value_km} AND
                    km < {km_range_end}
            )
            
            SELECT
                make,
                model,
                colour,
                fuel_type,
                year,
                gear,
                ROUND(AVG(price)) AS price
            FROM car_prices
            GROUP BY 
                make,
                model,
                colour,
                fuel_type,
                year,
                gear
        ''')

        # Store query results
        query_result = cursor.fetchall()

        total_num_query_result = len(query_result)

        # Check if the query produced any results
        if total_num_query_result > 0:
            # Upack data from query results
            make = query_result[0][0]
            model = query_result[0][1]
            colour = query_result[0][2]
            fuel_type = query_result[0][3]
            year = query_result[0][4]
            gear = query_result[0][5]
            kilometers = form_value_km
            estimated_value = locale.currency(query_result[0][6], grouping=True)
            estimated_value = estimated_value.replace('Eu', '€')
            estimated_value = estimated_value.replace(',00', '')

            return render_template('results.html', make=make, model=model, colour=colour, fuel_type=fuel_type, year=year, gear=gear, kilometers=kilometers, estimated_value=estimated_value)
        else:

            make = request.form['make']
            model = request.form['model']
            colour = request.form['colour']
            fuel_type =  request.form['fuelType']
            year = request.form['year']
            gear = request.form['gear']
            kilometers = request.form['km']
            message = 'No data for your criteria. Please try again later'

            return render_template('no-results.html', make=make, model=model, colour=colour, fuel_type=fuel_type, year=year, gear=gear, kilometers=kilometers, message=message)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)