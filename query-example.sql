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
	FROM alfa_romeo_car_prices_tbl AS cp
	JOIN alfa_romeo_make_and_model_tbl AS cm
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
		make = 'Alfa Romeo' AND
		model = 'Giulietta' AND
		colour = 'nero' AND
		fuel_type = 'Diesel' AND
		year = 2014 AND 
		gear = 'Manuale' AND
		km >= 160000 AND
		km < 170000
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