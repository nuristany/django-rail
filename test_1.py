import psycopg2
from psycopg2 import OperationalError

# Directly use credentials without config
DATABASE_NAME = 'railway'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'hEmXVqdPckpAnWgcROXBOvUesZHvrvAN'
DATABASE_HOST = 'postgres.railway.internal'  # Change as needed
DATABASE_PORT = '5432'

try:
    connection = psycopg2.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
        # Remove sslmode if not required
    )
    print("Connection successful")
except OperationalError as e:
    print(f"Connection failed: {e}")
finally:
    if 'connection' in locals() and connection:
        connection.close()
