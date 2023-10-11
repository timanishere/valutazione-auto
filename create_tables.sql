CREATE TABLE "alfa_romeo_make_and_model_tbl" (
    "make_and_model_id" serial   NOT NULL,
    "make" VARCHAR(200)   NOT NULL,
    "model" VARCHAR(200)   NOT NULL,
    "autoscout_url_make" VARCHAR(200)   NOT NULL,
    "autoscout_url_model" VARCHAR(200)   NOT NULL,
    CONSTRAINT "pk_alfa_romeo_make_and_model_tbl" PRIMARY KEY (
        "make_and_model_id"
     )
);

INSERT INTO audi_make_and_model_tbl (make, model, autoscout_url_make, autoscout_url_model)
VALUES
    ('Audi', '100', 'audi', '100'),
    ('Audi', '200', 'audi', '200'),
    ('Audi', '50', 'audi', '50'),
    ('Audi', '80', 'audi', '80'),
    ('Audi', '90', 'audi', '90'),
    ('Audi', 'A1', 'audi', 'a1'),
    ('Audi', 'A2', 'audi', 'a2'),
    ('Audi', 'A3', 'audi', 'a3'),
    ('Audi', 'A4', 'audi', 'a4'),
    ('Audi', 'A4 allroad', 'audi', 'a4-allroad'),
    ('Audi', 'A5', 'audi', 'a5'),
    ('Audi', 'A6', 'audi', 'a6'),
    ('Audi', 'A6 allroad', 'audi', 'a6-allroad'),
    ('Audi', 'A7', 'audi', 'a7'),
    ('Audi', 'A8', 'audi', 'a8'),
    ('Audi', 'Allroad', 'audi', 'allroad'),
    ('Audi', 'Altro', 'audi', 'altro'),
    ('Audi', 'Cabriolet', 'audi', 'cabriolet'),
    ('Audi', 'Coupe', 'audi', 'coupe'),
    ('Audi', 'e-tron', 'audi', 'e-tron'),
    ('Audi', 'e-tron GT', 'audi', 'e-tron-gt'),
    ('Audi', 'Q1', 'audi', 'q1'),
    ('Audi', 'Q2', 'audi', 'q2'),
    ('Audi', 'Q3', 'audi', 'q3'),
    ('Audi', 'Q4 e-tron', 'audi', 'q4-e-tron'),
    ('Audi', 'Q5', 'audi', 'q5'),
    ('Audi', 'Q7', 'audi', 'q7'),
    ('Audi', 'Q8', 'audi', 'q8'),
    ('Audi', 'Q8 e-tron', 'audi', 'q8-e-tron'),
    ('Audi', 'Quattro', 'audi', 'quattro'),
    ('Audi', 'R8', 'audi', 'r8'),
    ('Audi', 'RS', 'audi', 'rs'),
    ('Audi', 'RS Q3', 'audi', 'rs-q3'),
    ('Audi', 'RS Q5', 'audi', 'rs-q5'),
    ('Audi', 'RS Q8', 'audi', 'rs-q8'),
    ('Audi', 'RS2', 'audi', 'rs2'),
    ('Audi', 'RS3', 'audi', 'rs3'),
    ('Audi', 'RS4', 'audi', 'rs4'),
    ('Audi', 'RS5', 'audi', 'rs5'),
    ('Audi', 'RS6', 'audi', 'rs6'),
    ('Audi', 'RS7', 'audi', 'rs7'),
    ('Audi', 'S1', 'audi', 's1'),
    ('Audi', 'S2', 'audi', 's2'),
    ('Audi', 'S3', 'audi', 's3'),
    ('Audi', 'S4', 'audi', 's4'),
    ('Audi', 'S5', 'audi', 's5'),
    ('Audi', 'S6', 'audi', 's6'),
    ('Audi', 'S7', 'audi', 's8'),
    ('Audi', 'SQ2', 'audi', 'sq2'),
    ('Audi', 'SQ3', 'audi', 'sq3'),
    ('Audi', 'SQ5', 'audi', 'sq7'),
    ('Audi', 'SQ8', 'audi', 'sq8'),
    ('Audi', 'TT', 'audi', 'tt'),
    ('Audi', 'TT RS', 'audi', 'tt-rs'),
    ('Audi', 'TTS', 'audi', 'tts'),
    ('Audi', 'V8', 'audi', 'v8')


CREATE TABLE "alfa_car_prices_tbl" (
    "price_id" SERIAL NOT NULL,
    "make_and_model_id" INT,
    "year_id" INT,
    "colour_id" INT,
    "gear_id" INT,
    "fuel_type_id" INT,
    "km" INT,
    "kw" INT,
    CONSTRAINT "pk_audi_car_prices_tbl" PRIMARY KEY (
        "price_id"
     )
);