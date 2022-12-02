from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT INTO cities (name, country_id, visted) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)