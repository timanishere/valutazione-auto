# import psycopg2 module to connect to PostgreSQL database
import psycopg2

# import 'os' to access environment variables.
import os

# Import beautifulsoup library for webscraping
from bs4 import BeautifulSoup

# Import requests library to request infomation from websites
import requests

# import psycopg2.extras module to return data as a tuple
import psycopg2.extras

# EXTRACT DATA: STARTS

# Configure headers to send fake user agent with every request. This fixes 403 response when making a response
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

# Check connection
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

    # Open a cursor to perform SQL operationan and return data as a dictionary
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Query database to get list of colours
    cursor.execute('SELECT colour, autoscout_url_colour FROM car_colour_tbl')

    # Fetch data from database
    colour_list_data_arr_raw = cursor.fetchall()

    # Set colour of car. Use index
    i = 2

    # Get colour name and key
    car_colour = colour_list_data_arr_raw[i][0]
    car_colour_key = colour_list_data_arr_raw[i][1]

    print('car_color: ' + car_colour)

    # Query database to get list car make and model
    cursor.execute('SELECT make,model,autoscout_url_make, autoscout_url_model FROM car_make_and_model_tbl')

    # Fetch data from database
    make_and_model_list_data_arr_raw = cursor.fetchall()

    # Set the make and model. Use index
    i = 0

    # Get make and model
    car_make = make_and_model_list_data_arr_raw[i][0]
    car_model = make_and_model_list_data_arr_raw[i][1]
    car_make_key = make_and_model_list_data_arr_raw[i][2]
    car_model_key = make_and_model_list_data_arr_raw[i][3]
    
    print('car_make: ' + car_make)
    print('car_model: ' + car_model)

except Exception as error:
        print(error)
        print('Could not connect to db')

# The main page to scrape data from
main_site = 'https://www.autoscout24.it/lst/' + car_make_key + '/' + car_model_key + '/' + car_colour_key + '?atype=C&cy=I&damaged_listing=exclude&desc=0&powertype=kw&search_id=1s8324o1du&sort=standard&source=homepage_search-mask&ustate=N%2CU'

# Print messsage in terminal to know that scraping is in progress
print(f'Scraping {main_site} in progress...')

# Get information from the webpage
webpage = requests.get(main_site, headers=HEADERS,).text

# Create instance of beautifulsoup for the webpage
soup = BeautifulSoup(webpage, 'lxml')

# Get advert listing elements
advert_containers_arr = soup.findAll('article', class_='cldt-summary-full-item listing-impressions-tracking list-page-item false ListItem_article__ppamD')


# Create a loop to print out the details of all adverts
for advert_container in advert_containers_arr:

    # Get vehicle details container
    vehicle_details_container = advert_container.find('div', class_='VehicleDetailTable_container__mUUbY')

    # Get vehicle details items
    vehicle_details_item_raw = vehicle_details_container.findAll('span', class_='VehicleDetailTable_item__koEV4')

    try: 
        # Get price
        vehicle_price = advert_container.find('p', class_='Price_price__WZayw PriceAndSeals_current_price__XscDn').text
    except:
        vehicle_price = advert_container.find('span', class_='SuperDeal_highlightContainer__EPrZr').text

    vehicle_price = vehicle_price.replace(',-', '')
    vehicle_price = vehicle_price.split(' ')
    vehicle_price = vehicle_price[1]
    vehicle_price = vehicle_price.replace('.', '')

    # Convert item into array
    km_raw = vehicle_details_item_raw[0]

    # Convert object into a string
    km_raw = str(km_raw)

    # Convert item to an array
    km_raw = km_raw.split('></use></svg>')

    # Remove the characters from the string
    km = km_raw[1].replace('km</span>', '')
    km = km.replace('.', '')
    km = km.replace(' ', '')

    # Convert item into array
    gear_raw = vehicle_details_item_raw[1]

    # Convert object into a string
    gear_raw = str(gear_raw)

    # Convert item to an array
    gear_raw = gear_raw.split('></use></svg>')

    # Remove <span. to get string
    gear = gear_raw[1].replace('</span>', '')

    # Convert item into array
    year_raw = vehicle_details_item_raw[2]

    # Convert object into a string
    year_raw = str(year_raw)

    # Convert item to an array
    year_raw = year_raw.split('></use></svg>')

    # Remove <span> to get string
    year_raw = year_raw[1].replace('</span>', '').split('/')

    # Select the year
    year = year_raw[1]

    # Convert item into array
    fuel_type_raw = vehicle_details_item_raw[3]

    # Convert object into a string
    fuel_type_raw = str(fuel_type_raw)

    # Convert item to an array
    fuel_type_raw = fuel_type_raw.split('></use></svg>')

    # Remove <span> to get string
    fuel_type = fuel_type_raw[1].replace('</span>', '')

    # Convert item into array
    kw_raw = vehicle_details_item_raw[4]

    # Convert object into a string
    kw_raw = str(kw_raw)

    # Convert item to an array
    kw_raw = kw_raw.split('></use></svg>')

    # Remove <span> to get string
    kw_raw = kw_raw[1].replace('</span>', '').split(' ')

    kw = kw_raw[0]

    print(f'{car_make}|{car_model}|{car_colour}|{year}|{gear}|{fuel_type}|{kw}|{km}|{vehicle_price}')
    # EXTRACT DATA: ENDS


# Retrieve environment variables using os.environ.get('VARIABLE_NAME')
# db_host = os.environ.get('DB_HOST')
# db_name = os.environ.get('DB_NAME')
# db_user = os.environ.get('DB_USER')
# db_password = os.environ.get('DB_PASSWORD')
# db_port = os.environ.get('DB_PORT')

# Define database info
# hostname = db_host
# database = db_name
# username = db_user
# pwd = db_password
# port_id = db_port

# # Reset connection and cursor
# conn = None
# cursor = None

# # Check connection
# try:
#     # Connect to database
#     conn = psycopg2.connect(
#         host = hostname,
#         dbname = database,
#         user = username,
#         password = pwd,
#         port = port_id
#     )

#     # Open a cursor to perform SQL operationa
#     cursor = conn.cursor()

#     # Insert data into table
#     insert_script = 'INSERT INTO car_prices_tbl (price_id, make_id, model_id, year_id, colour_id, gear_id, fuel_type_id, km, km_range, kw, price) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
#     insert_values = ('3', '1', '1', '16', '3', '1', '1', '20453', '20000-30000', '61', '100')

#     # Execute insert script to insert values into the table
#     cursor.execute(insert_script, insert_values)

#     # Commit execution
#     conn.commit()
#     print('Added to db')

# except Exception as error:
#         print(error)
#         print('Could not connect to db')