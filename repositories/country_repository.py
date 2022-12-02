from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name, language, continent) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.language, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    selected_countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        new_country = Country(row['name'], row['language'], row['continent'], row['id'])
        selected_countries.append(new_country)
    return selected_countries


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)