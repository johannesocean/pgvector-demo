import os
import psycopg2


def create_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="testuser",
            password="testpwd",
            port=5432
        )
        yield conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting", error)
    finally:
        conn.close()


with create_db_connection() as connection:
    cur = connection.cursor()
    cur.execute("""""")
    connection.commit()
    cur.close()
