import sqlite3


def db_connect():
    conn = None
    try:
        conn = sqlite3.connect("../guardianDB.sqlite")
    except sqlite3.error as e:
        print(e)

    return conn


def db_init(conn):
    cursor = conn.cursor()
    schema = open("../schema.sql")
    query = schema.read()
    cursor.executescript(query)


def auth_user(conn, username, password):
    cursor = conn.cursor()
    query = f""" SELECT *
                FROM user
                WHERE username = {username} and password = {password}"""
    return query


if __name__ == '__main__':
    conn = db_connect()
    db_init(conn)
