import psycopg2

from app.db.config import db_config


def create_db_connection():
    params = db_config()
    try:
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting", error)
    return None
