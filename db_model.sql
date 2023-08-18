-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.




CREATE TABLE "car_prices_tbl" (
    "price_id" serial   NOT NULL,
    "make_and_model_id" int   NOT NULL,
    "year_id" int   NOT NULL,
    "colour_id" int   NOT NULL,
    "gear_id" int   NOT NULL,
    "fuel_type_id" int   NOT NULL,
    "km" varchar(200)   NOT NULL,
    "km_range" varchar(200)   NOT NULL,
    "kw" varchar(200)   NOT NULL,
    "price" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_prices_tbl" PRIMARY KEY (
        "price_id"
     )
);

ALTER TABLE "car_prices_tbl" ADD CONSTRAINT "fk_car_prices_tbl_make_id" FOREIGN KEY("make_id")
REFERENCES "car_make_tbl" ("make_id");

ALTER TABLE "car_prices_tbl" ADD CONSTRAINT "fk_car_prices_tbl_model_id" FOREIGN KEY("model_id")
REFERENCES "car_model_tbl" ("model_id");

ALTER TABLE "car_prices_tbl" ADD CONSTRAINT "fk_car_prices_tbl_year_id" FOREIGN KEY("year_id")
REFERENCES "car_year_tbl" ("year_id");

ALTER TABLE "car_prices_tbl" ADD CONSTRAINT "fk_car_prices_tbl_colour_id" FOREIGN KEY("colour_id")
REFERENCES "car_colour_tbl" ("colour_id");

ALTER TABLE "car_prices_tbl" ADD CONSTRAINT "fk_car_prices_tbl_gear_id" FOREIGN KEY("gear_id")
REFERENCES "car_gear_tbl" ("gear_id");

ALTER TABLE "car_prices_tbl" ADD CONSTRAINT "fk_car_prices_tbl_fuel_type_id" FOREIGN KEY("fuel_type_id")
REFERENCES "car_fuel_type_tbl" ("fuel_type_id");

