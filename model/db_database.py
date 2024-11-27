# model/db_database.py
import mysql.connector

# Variables globales para la conexión y el cursor
mydb = None
mycursor = None

# Función para conectar a la base de datos y obtener el cursor
def connect_db():
    global mydb, mycursor
    if mydb is None or not mydb.is_connected():  # Comprobamos si la conexión está activa
        try:
            # Crear una nueva conexión si no está activa
            mydb = mysql.connector.connect(
                host="localhost",        # Dirección del servidor
                user="root",             # Usuario de MySQL
                password="root",         # Contraseña del usuario de MySQL
                database="Hospital"      # Nombre de la base de datos
            )
            if mydb.is_connected():
                print("Conexión exitosa a la base de datos.")
            # Crear el cursor solo si la conexión es exitosa
            mycursor = mydb.cursor()
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            mydb = None
            mycursor = None
    return mydb, mycursor  # Retornamos la conexión y el cursor si es necesario