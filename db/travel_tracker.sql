DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    language VARCHAR(255),
    continent VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    capital_city BOOLEAN,
    review TEXT,
    country_id INT NOT NULL REFERENCES countries(id)
);


    -- do i need user_id in cities?
    -- should country_id in cities be SERIAL NOT NULL REFERENCES countries(id)
