from db.run_sql import run_sql

from models.memory import Memory
from models.user import User
from models.country import Country

from repositories import user_repository, country_repository

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


def select_all():
    selected_memories = []

    sql = "SELECT * FROM memories"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select_user_by_id(row['user_id'])
        location = country_repository.select_country_by_id(row['country_id'])
        new_memory = Memory(user, location, row['memory'], row['id'])
        selected_memories.append(new_memory)
    return selected_memories


def delete(id):
    sql = "DELETE FROM memories WHERE id=%s"
    values = [id]
    run_sql(sql, values)