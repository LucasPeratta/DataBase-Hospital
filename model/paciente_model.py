from model.db_database import mycursor, mydb, connect_db

mydb, mycursor = connect_db()  # Esto asegura que mydb y mycursor son válidos después de la conexión


def registrarPaciente(nombre, edad, dni, genero, direccion, telefono):
    try:
        # Define la consulta SQL
        sql = "INSERT INTO paciente (nombre, edad, dni, genero, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nombre, edad, dni, genero, direccion, telefono)

        # Ejecutar la consulta SQL
        mycursor.execute(sql, val)
        mydb.commit()

        # Obtener el ID del paciente recién insertado
        id_paciente = mycursor.lastrowid

        # Mostrar los datos del paciente, incluyendo el ID
        print("-Paciente creado con éxito-")
        print(f"ID: {id_paciente}, Nombre: {nombre}, Edad: {edad}, DNI: {dni}, Género: {genero}, Dirección: {direccion}, Teléfono: {telefono}")
    except Exception as e:
        # Capturar el error y mostrarlo
        print("\nError al crear paciente:", e)


def mostrarTodos():
    mycursor.execute("SELECT * FROM paciente")
    resultados = mycursor.fetchall()
    for registro in resultados:
        print(registro)  

def buscarPorDni(dni):
    mycursor.execute(f"SELECT * FROM paciente WHERE dni = %s", (dni,))
    resultado = mycursor.fetchone()  # Obtener un solo registro
    if resultado:  
        print("La informacion del paciente es la siguiente:")
        print(resultado)
    else: 
        print("No se encontró ningún paciente con el DNI:", dni)

def EliminarPaciente(id):
    # Ejecutamos la consulta para verificar si el paciente existe
    mycursor.execute(f"SELECT * FROM paciente WHERE id_paciente = %s", (id,))
    resultado = mycursor.fetchone()  

    if resultado:  
        sql = "DELETE FROM paciente WHERE id_paciente = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Paciente con ID {id} eliminado con éxito.")
    else:  
        print(f"No se encontró ningún paciente con el ID: {id}")


def modificarPaciente(id, nombre, edad, dni, genero, direccion, telefono):
    try:
        # Verificar si el paciente existe
        mycursor.execute("SELECT * FROM paciente WHERE id_paciente = %s", (id,))
        resultado = mycursor.fetchone()
        
        if resultado:  # Si el paciente existe
            sql = """UPDATE paciente 
                     SET nombre = %s, edad = %s, dni = %s, genero = %s, direccion = %s, telefono = %s 
                     WHERE id_paciente = %s"""
            val = (nombre, edad, dni, genero, direccion, telefono, id)
            mycursor.execute(sql, val)
            mydb.commit()  # Confirmar los cambios en la base de datos
            
            print("Registro actualizado con éxito.")
        else:  # Si el paciente no existe
            print(f"No se encontró ningún paciente con el ID: {id}")
    
    except Exception as e:
        print(f"\nHubo un error al modificar el paciente: {e}")
