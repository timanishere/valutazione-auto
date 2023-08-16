-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "car_make_and_model" (
    "make_and_model_id" int   NOT NULL,
    "make" varchar(200)   NOT NULL,
    "model" varchar(200)   NOT NULL,
    "autoscout_url_make" varchar(200)   NOT NULL,
    "autoscout_url_model" varchar(200)   NOT NULL,
    CONSTRAINT "pk_car_make_and_model" PRIMARY KEY (
        "make_and_model_id"
     )
);

