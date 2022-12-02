from db.run_sql import run_sql

from models.city import City

# def save(city):
#     sql = "INSERT INTO cities (name, country, capital_city, population, visited, review) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
#     values = [city.name, city.country, city.capital_city, city.population, city.visited, city.review]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     city.id = id
#     return city
