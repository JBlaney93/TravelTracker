DROP TABLE IF EXISTS memories;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS countries;



CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cities VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE memories (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    memory TEXT
);



