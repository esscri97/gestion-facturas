import psycopg2

DB_CONFIG = {
    "dbname": "crm",
    "user": "postgres",
    "password": "postgres",
    "host": "127.0.0.1",
    "port": 5432,
    "client_encoding": "UTF8" # Asegúrate de que esta línea esté, si quieres ser explícito
}

def connect():
    try:
        conn = psycopg2.connect(
            dbname="crm",
            user="user",
            password="password",
            host="127.0.0.1",
            port=5432
        )
        conn.set_client_encoding('UTF8')
        print("Conexión exitosa a la base de datos!")
        print(f"Codificación del cliente: {conn.encoding}")
        return conn
    except Exception as e:
        print("Error al conectar con la base de datos:")
        print(repr(e))
        raise

if __name__ == '__main__':
    connection = connect()
    if connection:
        connection.close()