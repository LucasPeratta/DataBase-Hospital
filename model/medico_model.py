from model.db_database import mycursor, mydb, connect_db


# Función para registrar un nuevo médico
def registrar_medico(nombre, especialidad, telefono):
    try:
        # Asegurarse de que los datos no estén vacíos
        if not nombre or not especialidad or not telefono:
            print("Todos los campos son obligatorios.")
            return
        
        sql = "INSERT INTO medico (nombre, especialidad, telefono) VALUES (%s, %s, %s)"
        val = (nombre, especialidad, telefono)

        # Ejecutar la consulta SQL
        mycursor.execute(sql, val)
        mydb.commit()

        print("- Médico registrado con éxito -")
    except Exception as e:
        print("\nError al registrar médico:", e)


# Función para actualizar los detalles de un médico
def actualizar_medico(id_medico, nombre=None, especialidad=None, telefono=None):
    try:
        # Verificar si el médico existe
        mycursor.execute("SELECT * FROM medico WHERE id_medico = %s", (id_medico,))
        resultado = mycursor.fetchone()

        if resultado:  # Si el médico existe
            campos = []
            valores = []

            if nombre:
                campos.append("nombre = %s")
                valores.append(nombre)
            if especialidad:
                campos.append("especialidad = %s")
                valores.append(especialidad)
            if telefono:
                campos.append("telefono = %s")
                valores.append(telefono)

            if campos:
                sql = f"UPDATE medico SET {', '.join(campos)} WHERE id_medico = %s"
                valores.append(id_medico)
                mycursor.execute(sql, valores)
                mydb.commit()

                print("Datos del médico actualizados con éxito.")
            else:
                print("No se proporcionaron campos para actualizar.")
        else:  # Si el médico no existe
            print(f"No se encontró ningún médico con el ID: {id_medico}")

    except Exception as e:
        print(f"\nError al actualizar el médico: {e}")


# Función para eliminar un médico
def eliminar_medico(id_medico):
    try:
        # Verificar si el médico existe
        mycursor.execute("SELECT * FROM medico WHERE id_medico = %s", (id_medico,))
        resultado = mycursor.fetchone()

        if resultado:  # Si el médico existe
            sql = "DELETE FROM medico WHERE id_medico = %s"
            mycursor.execute(sql, (id_medico,))
            mydb.commit()

            print(f"Médico con ID {id_medico} eliminado con éxito.")
        else:  # Si el médico no existe
            print(f"No se encontró ningún médico con el ID: {id_medico}")

    except Exception as e:
        print(f"\nError al eliminar el médico: {e}")


# Función para buscar un médico por nombre
def buscar_medico_por_nombre(nombre):
    try:
        sql = "SELECT * FROM medico WHERE nombre LIKE %s"
        mycursor.execute(sql, ('%' + nombre + '%',))
        resultados = mycursor.fetchall()

        if resultados:
            for medico in resultados:
                print(medico)
        else:
            print(f"No se encontraron médicos con el nombre: {nombre}")
    
    except Exception as e:
        print(f"\nError al buscar el médico por nombre: {e}")


# Función para obtener todos los médicos
def obtener_todos_los_medicos():
    try:
        sql = "SELECT * FROM medico"
        mycursor.execute(sql)
        resultados = mycursor.fetchall()

        if resultados:
            for medico in resultados:
                print(medico)
        else:
            print("No se encontraron médicos registrados.")
    
    except Exception as e:
        print(f"\nError al obtener todos los médicos: {e}")
