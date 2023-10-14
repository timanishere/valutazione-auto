# Import flask
from flask import Flask, render_template, request, redirect, url_for

# import psycopg2 module to connect to PostgreSQL database
import psycopg2

# import psycopg2.extras module to return data as a tuple
import psycopg2.extras

# import 'os' to access environment variables.
import os

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

# Define route
@app.route('/valutazione-auto')

# Define webpage
def index():
    return render_template('index.html')



# Create route for getting data
@app.route('/valutazione-auto/risultato', methods = ['POST'])

# Create insert function
def results():
    # Check if request is POST
    if request.method == 'POST':

        form_value_make = request.form['make']
        form_value_model = request.form['model']
        form_value_year = request.form['year']
        form_value_colour = request.form['colour']
        form_value_gear = request.form['gear']
        form_value_fuelType = request.form['fuelType']
        form_value_km = request.form['km']

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
                FROM audi_car_prices_tbl AS cp
                JOIN audi_make_and_model_tbl AS cm
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
                    km >= {form_value_km}
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

        # Upack data from query results
        make = query_result[0][0]
        model = query_result[0][1]
        colour = query_result[0][2]
        fuel_type = query_result[0][3]
        year = query_result[0][4]
        gear = query_result[0][5]
        kilometers = form_value_km
        estimated_value = query_result[0][6]

        print(f'Estimated value for {make} {model} {year} is {estimated_value}')

    return render_template('results.html', make=make, model=model, colour=colour, fuel_type=fuel_type, year=year, gear=gear, kilometers=kilometers, estimated_value=estimated_value)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)