from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries (name, user_id, continent) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.user.id, country.continent]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


# def select_all():
#     selected_countries = []

#     sql = "SELECT * FROM countries"
#     results = run_sql(sql)
#     for row in results:
#         new_country = Country(row['name'], row['continent'], row['id'])
#         selected_countries.append(new_country)
#     return selected_countries


# def select_country_by_id(id):
#     selected_country = None
#     sql = "SELECT * FROM countries WHERE id=%s"
#     values = [id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         selected_country = Country(result['name'], result['continent'], result['id'])
#     return selected_country


# def delete_all():
#     sql = "DELETE FROM countries"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM countries WHERE id=%s"
#     values = [id]
#     run_sql(sql,values)

