SELECT 
    car_make_tbl.make
    car_model_tbl.model
    car_prices.prices
FROM car_make_tbl
JOIN car_model_tbl
    ON car_make_tbl.make = car_model_tbl.make
JOIN car_prices_tbl
    ON car_model_tbl.make = car_prices_tbl.make AND
    car_model_tbl.model = car_prices_tbl.model
WHERE
    make = 'fiat' AND
    model = '500'
    year = 2016 AND
    gear = 'manual' AND
    colour = 'white' AND
    doors = '3-4' AND 
    fuel = 'gas' AND
    kw = 61 AND
    emission = 'euro 6'