from model.db_database import mycursor, mydb

#Función para registrar un nuevo médico
def registrar_medico(nombre, especialidad, telefono):
    sql = "INSERT INTO Medico (nombre, especialidad, teléfono) VALUES (%s, %s, %s)"
    val = (nombre, especialidad, telefono)
    mycursor.execute(sql, val)
    mydb.commit()

#Función para actualizar los detalles de un médico
def actualizar_medico(id_medico, nombre=None, especialidad=None, telefono=None):
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
        sql = f"UPDATE Medico SET {', '.join(campos)} WHERE id_medico = %s"
        valores.append(id_medico)
        mycursor.execute(sql, valores)
        mydb.commit()

#Función para eliminar un médico
def eliminar_medico(id_medico):
    sql = "DELETE FROM Medico WHERE id_medico = %s"
    mycursor.execute(sql, (id_medico,))
    mydb.commit()

#Función para buscar un médico por nombre
def buscar_medico_por_nombre(nombre):
    sql = "SELECT * FROM Medico WHERE nombre LIKE %s"
    mycursor.execute(sql, ('%' + nombre + '%',))
    resultados = mycursor.fetchall()
    return resultados

#Función para obtener todos los médicos
def obtener_todos_los_medicos():
    sql = "SELECT * FROM Medico"
    mycursor.execute(sql)
    resultados = mycursor.fetchall()
    return resultados