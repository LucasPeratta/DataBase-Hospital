import mysql.connector
from mysql.connector import Error

def execute_sql_file(connection, file_path):
    """Lee y ejecuta el contenido de un archivo SQL."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        cursor = connection.cursor()
        for statement in sql_script.split(';'):  # Divide el script en múltiples sentencias SQL
            if statement.strip():  # Ejecuta solo las sentencias no vacías
                cursor.execute(statement)
        connection.commit()
        print(f"Archivo ejecutado con éxito: {file_path}")
    except Error as e:
        print(f"Error al ejecutar el archivo {file_path}: {e}")

def initialize_database():
    """Inicializa la base de datos leyendo y ejecutando los archivos SQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",             
            password="root"  
        )
        if connection.is_connected():
            print("Conexión exitosa a MySQL")
            # Ejecutar los scripts
            execute_sql_file(connection, 'database/tablas.sql')
            execute_sql_file(connection, 'database/insertTablas.sql')
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    initialize_database()
