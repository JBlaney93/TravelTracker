from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING *"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user


def select_all():
    selected_users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        new_user = User(row['name'], row['id'])
        selected_users.append(new_user)
    return selected_users


def select_user_by_id(id):
    selected_user = None
    sql = "SELECT * FROM users WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        selected_user = User(result['name'], result['id'])
    return selected_user


def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM users WHERE id=%s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE SET (name) VALUES=(%s) WHERE id=%s"
    values = [user.name, user.id]
    run_sql(sql, values)