from db.run_sql import run_sql

from models.memory import Memory

def save(memory):
    sql = "INSERT INTO memories (user_id, country_id, memory) VALUES (%s, %s, %s) RETURNING *"
    values = [memory.user.id, memory.country.id, memory.memory]
    results = run_sql(sql, values)
    id = results[0]['id']
    memory.id = id
    return memory


def delete_all():
    sql = "DELETE FROM memories"
    run_sql(sql)