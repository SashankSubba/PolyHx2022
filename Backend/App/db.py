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


def auth_user(conn, email, password):
    cursor = conn.cursor()
    query = f" SELECT * FROM user WHERE email = '{email}' and password = '{password}'"
    cursor.execute(query)
    record = cursor.fetchone()
    user = {
        "userId": record[0],
        "firstName": record[3],
        "lastName": record[4],
        "phoneNumber": record[5]
    }
    return user


def post_encounter(conn, data):
    cursor = conn.cursor()
    query = f"INSERT INTO encounter (userId, transcribedAudio, sentimentTags, latitude, longitude, resolved, isPrivate) VALUES ({data['userId']}, '{data['transcribedAudio']}', '{data['sentimentTags']}', {data['latitude']}, {data['longitude']}, {data['resolved']}, {data['isPrivate']});"
    cursor.execute(query)
    conn.commit()
    return cursor.rowcount()


def get_emergency_contacts(conn, phone_number):
    cursor = conn.cursor()
    query = f"SELECT emergencyNumber FROM contacts WHERE selfNumber = '{phone_number}';"
    cursor.execute(query)
    records = cursor.fetchall()
    list_of_numbers = []
    for row in records:
        list_of_numbers.append(row[0])
    return list_of_numbers


if __name__ == '__main__':
    conn = db_connect()
    db_init(conn)
