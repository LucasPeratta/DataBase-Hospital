# model/turno_model.py
from model.db_database import mycursor, mydb
import mysql.connector



# Función para programar un nuevo turno (cita)
def programarTurno(id_paciente, id_medico, fecha, hora):
    sql = """
    INSERT INTO Cita (id_paciente, id_medico, fecha_cita, hora_cita, estado)
    VALUES (%s, %s, %s, %s, 'Pendiente')
    """
    val = (id_paciente, id_medico, fecha, hora)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Turno programado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al programar el turno: {err}")

# Función para actualizar un turno existente
def actualizarTurno(id_cita, fecha=None, hora=None, estado=None):
    campos = []
    valores = []

    if fecha:
        campos.append("fecha_cita = %s")
        valores.append(fecha)
    if hora:
        campos.append("hora_cita = %s")
        valores.append(hora)
    if estado:
        campos.append("estado = %s")
        valores.append(estado)

    if campos:
        sql = f"UPDATE Cita SET {', '.join(campos)} WHERE id_cita = %s"
        valores.append(id_cita)
        try:
            mycursor.execute(sql, valores)
            mydb.commit()
            print(f"Turno con ID {id_cita} actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar el turno: {err}")
    else:
        print("No se proporcionaron campos para actualizar.")

# Función para cancelar un turno (cita)
def cancelarTurno(id_cita):
    sql = "DELETE FROM Cita WHERE id_cita = %s"
    try:
        mycursor.execute(sql, (id_cita,))
        mydb.commit()
        print(f"Turno con ID {id_cita} cancelado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al cancelar el turno: {err}")

# Función para ver los turnos de un paciente
def verTurnosPorPaciente(id_paciente):
    sql = "SELECT * FROM Cita WHERE id_paciente = %s"
    mycursor.execute(sql, (id_paciente,))
    resultados = mycursor.fetchall()
    if resultados:
        print("Turnos del paciente:")
        for turno in resultados:
            print(f"ID Cita: {turno[0]}, Médico ID: {turno[2]}, Fecha: {turno[3]}, Hora: {turno[4]}, Estado: {turno[5]}")
    else:
        print(f"No se encontraron turnos para el paciente con ID {id_paciente}.")

# Función para ver los turnos de un médico
def verTurnosPorMedico(id_medico):
    sql = "SELECT * FROM Cita WHERE id_medico = %s"
    mycursor.execute(sql, (id_medico,))
    resultados = mycursor.fetchall()
    if resultados:
        print("Turnos del médico:")
        for turno in resultados:
            print(f"ID Cita: {turno[0]}, Paciente ID: {turno[1]}, Fecha: {turno[3]}, Hora: {turno[4]}, Estado: {turno[5]}")
    else:
        print(f"No se encontraron turnos para el médico con ID {id_medico}.")
