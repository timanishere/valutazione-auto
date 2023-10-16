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

# Configure headers to send fake user agent with every request. This fixes 403 response when making a response
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

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

except Exception as error:
      print(error)
      print('Could not connect to db')

# Open a cursor to perform SQL operationan and return data as a dictionary
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Query database to get list car make and model
cursor.execute('SELECT make,model,autoscout_url_make, autoscout_url_model FROM mercedes_benz_make_and_model_tbl')

# Store make and model here
make_and_model_list_data_arr_raw = cursor.fetchall()

# Calculate how many make and models there are
number_of_make_and_model = len(make_and_model_list_data_arr_raw)

# Loop through every make and model
for i in range(84, number_of_make_and_model):

   # Get make and model details from DB
   car_make = make_and_model_list_data_arr_raw[i][0]
   car_model = make_and_model_list_data_arr_raw[i][1]
   car_make_key = make_and_model_list_data_arr_raw[i][2]
   car_model_key = make_and_model_list_data_arr_raw[i][3]

   # Query database to get list of colours
   cursor.execute('SELECT * FROM car_colour_tbl ORDER BY colour_id')

   # Fetch colour data from database
   colour_list_data_arr_raw = cursor.fetchall()

   # Calculate how many colours are in the DB
   number_of_colours = len(colour_list_data_arr_raw)

   # Query database to get list of years
   cursor.execute('SELECT year FROM car_year_tbl ORDER BY year')

   # Fetch years data from database
   year_list_data_arr_raw = cursor.fetchall()

   # Calculate how many years are in the DB
   number_of_years = len(year_list_data_arr_raw)

   # Loop through every colour
   for c in range(0, number_of_colours):

      # Get colour name and key
      car_colour = colour_list_data_arr_raw[c][1]
      car_colour_key = colour_list_data_arr_raw[c][2]

      # Loop through every year
      for y in range(0, number_of_years):
         car_year = year_list_data_arr_raw[y][0]
         car_year = str(car_year)

         print(f'Scraping year: {car_year}')

         # The main page to scrape data from
         # main_site = 'https://www.autoscout24.it/lst/' + car_make_key + '/' + car_model_key + '/' + car_colour_key + '?atype=C&cy=I&damaged_listing=exclude&desc=0&powertype=kw&search_id=1s8324o1du&sort=standard&source=homepage_search-mask&ustate=N%2CU&page=1'
         main_site = 'https://www.autoscout24.it/lst/' + car_make_key + '/' + car_model_key + '/' + car_colour_key + '?atype=C&cy=I&damaged_listing=exclude&desc=0&fregfrom=' + car_year + '&fregto=' + car_year + '&powertype=kw&search_id=1s8324o1du&sort=standard&source=homepage_search-mask&ustate=N%2CU&page='

         # Print messsage in terminal to know that scraping is in progress
         print(f'Scraping {main_site} in progress...')

         # Get information from the webpage
         webpage = requests.get(main_site, headers=HEADERS,).text

         # Create instance of beautifulsoup for the webpage
         soup = BeautifulSoup(webpage, 'lxml')

         # Get paginator
         number_of_pages_element_arr = soup.findAll('button', class_='FilteredListPagination_button__41hHM')

         # Get HTML container of the total number of cars
         try:
            total_cars_container = soup.find('div', class_='ListHeader_top__jY34N')

            # Extract the number
            total_cars_container = total_cars_container.find('h1')
            total_cars_container = total_cars_container.find('span')
            total_cars_container = total_cars_container.find('span').text
         except:

            total_cars_container = soup.find('div', class_='ListHeader_top__jY34N')

            if total_cars_container is not None:
               total_cars_container = total_cars_container.find('div', class_='NoResults_wrapper__hQZGf')

            # Extract the number
            total_cars_container = total_cars_container.find('h1')
            total_cars_container = total_cars_container.find('span')
            total_cars_container = total_cars_container.find('span').text

         # Convert to a string. Use to check how many cars there are for each criteria
         total_cars = int(total_cars_container)

         # Skip pages that do not have any results based on the criteria
         if total_cars > 0:
            try:
               # Get the last number of the page
               last_page_raw = number_of_pages_element_arr[2]
               last_page_raw = str(last_page_raw)
            except:
               last_page_raw = None

            # Clean string to get number
            try:
               last_page = last_page_raw.split('>')
               last_page = last_page[1]
               last_page = last_page.replace('</button', '')
               last_page = int(last_page)
               last_page = last_page + 1
            except:
               last_page = 3

            counter = 0

            # Loop through every page
            for p in range(1, last_page):

               # Print the page number getting scraped
               print(f'scraping page {p}')

               # Convert to string
               p = str(p)

               # The main page to scrape data from
               main_site_loop = 'https://www.autoscout24.it/lst/' + car_make_key + '/' + car_model_key + '/' + car_colour_key + '?atype=C&cy=I&damaged_listing=exclude&desc=0&fregfrom=' + car_year + '&fregto=' + car_year + '&powertype=kw&search_id=1s8324o1du&sort=standard&source=homepage_search-mask&ustate=N%2CU&page=' + p

               # Get information from mainsite
               webpage_loop = requests.get(main_site_loop, headers=HEADERS,).text

               # Create instance of beautifulsoup for webpage_loop
               soup = BeautifulSoup(webpage_loop, 'lxml')

               # Get advert listing elements
               advert_containers_arr = soup.findAll('article', class_='cldt-summary-full-item listing-impressions-tracking list-page-item false ListItem_article__ppamD')

               # Loop through array of adverts
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
                     vehicle_price = vehicle_price.split(',')
                     vehicle_price = vehicle_price[0]

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
                     
                  try:
                     km = int(km)
                  except:
                     km = 0

                  # km_start = km
                  # print(f'km_start: {km_start}')

                  # number_of_chars = len(km)

                  # zeros = ''

                  # for i in range(1, number_of_chars):
                  #     zeros = zeros + '0'

                  # number_to_add = '1' + zeros

                  # km_start = int(km_start)
                  # number_to_add = int(number_to_add)

                  # km_end = km_start + number_to_add
                  

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
                  try:
                     year = year_raw[1]
                  except: 
                     year = None

                  # Convert item into array
                  fuel_type_raw = vehicle_details_item_raw[3]

                  # Convert object into a string
                  fuel_type_raw = str(fuel_type_raw)

                  # Convert item to an array
                  fuel_type_raw = fuel_type_raw.split('></use></svg>')

                  # Remove <span> to get string
                  fuel_type = fuel_type_raw[1].replace('</span>', '')

                  if fuel_type == 'Elettrica/Benzina': 
                     fuel_type = 'Ibrida (Elettrica/Benzina)'

                  elif fuel_type == 'Elettrica/Diesel': 
                     fuel_type = 'Ibrida (Elettrica/Diesel)'

                  # Convert item into array
                  kw_raw = vehicle_details_item_raw[4]

                  # Convert object into a string
                  kw_raw = str(kw_raw)

                  # Convert item to an array
                  kw_raw = kw_raw.split('></use></svg>')

                  # Remove <span> to get string
                  kw_raw = kw_raw[1].replace('</span>', '').split(' ')

                  kw = kw_raw[0]
                  
                  try:
                     kw = int(kw)
                  except:
                     kw = None
                     
                  if year != None:
                     # Query database to the id of the year
                     cursor.execute(f'SELECT year_id FROM car_year_tbl WHERE year = {year}')

                     # Fetch data from database
                     year_id = cursor.fetchall()
                     year_id = year_id[0][0]

                  # Query database to the id of the color
                  cursor.execute(f"SELECT colour_id FROM car_colour_tbl WHERE colour = '{car_colour}'")

                  # Fetch data from database
                  colour_id = cursor.fetchall()
                  colour_id = colour_id[0][0]

                  try:
                     # Query database to the id of the gear
                     cursor.execute(f"SELECT gear_id FROM car_gear_tbl WHERE gear = '{gear}'")
                     
                     # Fetch data from database
                     gear_id = cursor.fetchall()
                     gear_id = gear_id[0][0]
                  except:
                     gear_id = 4

                  # Query database to the id of the gear
                  cursor.execute(f"SELECT fuel_type_id FROM car_fuel_type_tbl WHERE fuel_type = '{fuel_type}'")
                     
                  try:
                     # Fetch data from database
                     fuel_type_id = cursor.fetchall()
                     fuel_type_id = fuel_type_id[0][0]
                  except:
                     fuel_type_id = 9

                  # Query database to the id of the make and model
                  cursor.execute(f"SELECT make_and_model_id FROM mercedes_benz_make_and_model_tbl  WHERE make = '{car_make}' AND model = '{car_model}'")

                  # Fetch data from database
                  make_and_model_id = cursor.fetchall()
                  make_and_model_id = make_and_model_id[0][0]

                  # EXTRACT DATA: ENDS

                  # print(f'{make_and_model_id}|{year_id}|{colour_id}|{gear_id}|{fuel_type_id}|{km}|{kw}|{vehicle_price}')

                  # LOAD DATA: STARTS

                  # Insert data into table
                  insert_script = 'INSERT INTO mercedes_benz_car_prices_tbl (make_and_model_id, year_id, colour_id, gear_id, fuel_type_id, km, kw, price) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                  insert_values = (make_and_model_id, year_id, colour_id, gear_id, fuel_type_id, km, kw, vehicle_price)

                  # Execute insert script to insert values into the table
                  cursor.execute(insert_script, insert_values)

                  # Commit execution
                  conn.commit()

                  print('Added to db')
         else:
            print('Skipping')