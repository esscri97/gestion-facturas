import psycopg2

DB_CONFIG = {
    "dbname": "crm",
    "user": "user",
    "password": "1234",
    "host": "127.0.0.1",
    "port": 5432
}

def connect():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print("Error al conectar con la base de datos:")
        print(repr(e)) 
        raise