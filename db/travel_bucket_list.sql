CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARHCAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARHCAR(255),
    language VARHCAR(255),
    continent VARHCAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARHCAR(255),
    country VARHCAR(255),
    capital_city BOOLEAN,
    review TEXT,
    country_id INT REFERENCES countries(id)  
);
