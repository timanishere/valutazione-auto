-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "car_make_tbl" (
    "make_id" int   NOT NULL,
    "make" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_make_tbl" PRIMARY KEY (
        "make_id"
     )
);

CREATE TABLE "car_model_tbl" (
    "model_id" int   NOT NULL,
    "model" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_model_tbl" PRIMARY KEY (
        "model_id"
     )
);

CREATE TABLE "car_year_tbl" (
    "year_id" int   NOT NULL,
    "year" int   NOT NULL,
    CONSTRAINT "pk_car_year_tbl" PRIMARY KEY (
        "year_id"
     )
);

CREATE TABLE "car_colour_tbl" (
    "colour_id" int   NOT NULL,
    "colour" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_colour_tbl" PRIMARY KEY (
        "colour_id"
     )
);

CREATE TABLE "car_gear_tbl" (
    "gear_id" int   NOT NULL,
    "gear" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_gear_tbl" PRIMARY KEY (
        "gear_id"
     )
);

CREATE TABLE "car_fuel_type_tbl" (
    "fuel_type_id" int   NOT NULL,
    "fuel_type" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_fuel_type_tbl" PRIMARY KEY (
        "fuel_type_id"
     )
);

CREATE TABLE "car_prices_tbl" (
    "price_id" int   NOT NULL,
    "make_id" int   NOT NULL,
    "model_id" int   NOT NULL,
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

