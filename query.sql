SELECT
	cmm.make,
	cmm.model,
	cc.colour,
	cy.year,
	cg.gear,
	cft.fuel_type,
	cp.km, 
	cp.kw,
	cp.price
	
FROM car_prices_tbl AS cp
INNER JOIN fiat_make_and_model_tbl AS cmm
	ON cp.make_and_model_id = cmm.make_and_model_id
INNER JOIN car_year_tbl AS cy
	ON cp.year_id = cy.year_id
INNER JOIN car_colour_tbl AS cc
	ON cp.colour_id = cc.colour_id
INNER JOIN car_gear_tbl AS cg
	ON cp.gear_id = cg.gear_id
INNER JOIN car_fuel_type_tbl AS cft
	ON cp.fuel_type_id = cft.fuel_type_id
WHERE
	cmm.make = 'Fiat' AND
	cmm.model = '500' AND
	cc.colour = 'bianco' AND 
	cy.year = 2010 AND
	cg.gear = 'Manuale' AND
	cft.fuel_type = 'Benzina' AND
	cp.km >= 140000 AND cp.km < 170000 AND
	cp.kw = 51
ORDER BY cp.price