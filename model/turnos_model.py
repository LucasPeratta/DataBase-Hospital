from model.db_database import mycursor, mydb, connect_db
import mysql.connector
import datetime

mydb, mycursor = connect_db()  # Esto asegura que mydb y mycursor son válidos después de la conexión

# Función para validar si un paciente existe
def pacienteExiste(id_paciente):
    sql = "SELECT 1 FROM paciente WHERE id_paciente = %s"
    mycursor.execute(sql, (id_paciente,))
    return mycursor.fetchone() is not None

# Función para validar si un médico existe
def medicoExiste(id_medico):
    sql = "SELECT 1 FROM medico WHERE id_medico = %s"
    mycursor.execute(sql, (id_medico,))
    return mycursor.fetchone() is not None

# Función para validar la fecha y hora
def validarFechaHora(fecha, hora):
    try:
        # Validar formato de fecha (yyyy-mm-dd) y hora (HH:MM)
        datetime.datetime.strptime(fecha, "%Y-%m-%d")
        datetime.datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

# Función para programar un nuevo turno (cita)
def programarTurno(id_paciente, id_medico, fecha, hora):
    if not pacienteExiste(id_paciente):
        print(f"No se encontró un paciente con ID {id_paciente}.")
        return
    if not medicoExiste(id_medico):
        print(f"No se encontró un médico con ID {id_medico}.")
        return
    if not validarFechaHora(fecha, hora):
        print("El formato de la fecha o la hora es incorrecto.")
        return

    sql = """
    INSERT INTO cita (id_paciente, id_medico, fecha_cita, hora_cita, estado)
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
    # Verificar si el turno existe
    mycursor.execute("SELECT * FROM cita WHERE id_cita = %s", (id_cita,))
    if not mycursor.fetchone():
        print(f"No se encontró el turno con ID {id_cita}.")
        return

    # Validar datos proporcionados
    if fecha and not validarFechaHora(fecha, hora):
        print("El formato de la fecha o la hora es incorrecto.")
        return

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
        sql = f"UPDATE cita SET {', '.join(campos)} WHERE id_cita = %s"
        valores.append(id_cita)
        try:
            mycursor.execute(sql, valores)
            mydb.commit()
            print(f"Turno con ID {id_cita} actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar el turno: {err}")
    else:
        print("No se proporcionaron campos para actualizar.")

# Función para ver y cancelar las citas de un médico
def cancelarTurnoPorMedico(id_medico):
    # Verificar si el médico existe
    if not medicoExiste(id_medico):
        print(f"No se encontró un médico con ID {id_medico}.")
        return

    # Obtener las citas del médico
    sql = """
    SELECT cita.id_cita, paciente.nombre AS paciente_nombre, cita.fecha_cita, cita.hora_cita, cita.estado
    FROM cita
    JOIN paciente ON cita.id_paciente = paciente.id_paciente
    WHERE cita.id_medico = %s
    """
    mycursor.execute(sql, (id_medico,))
    resultados = mycursor.fetchall()

    if not resultados:
        print(f"No se encontraron citas para el médico con ID {id_medico}.")
        return

    print("Citas del médico:")
    # Mostrar las citas del médico
    for turno in resultados:
        print(f"ID Cita: {turno[0]}, Paciente: {turno[1]}, Fecha: {turno[2]}, Hora: {turno[3]}, Estado: {turno[4]}")

    # Solicitar al usuario que ingrese el ID de la cita a cancelar
    id_cita = input("Ingrese el ID de la cita que desea cancelar: ")

    # Verificar si la cita existe
    mycursor.execute("SELECT * FROM cita WHERE id_cita = %s", (id_cita,))
    if not mycursor.fetchone():
        print(f"No se encontró el turno con ID {id_cita}.")
        return

    # Proceder a cancelar la cita
    sql = "DELETE FROM cita WHERE id_cita = %s"
    try:
        mycursor.execute(sql, (id_cita,))
        mydb.commit()
        print(f"Turno con ID {id_cita} cancelado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al cancelar el turno: {err}")


from datetime import datetime

def cancelarTurnoPorFechas(id_medico):
    # Verificar si el médico existe
    if not medicoExiste(id_medico):
        print(f"No se encontró un médico con ID {id_medico}.")
        return

    # Solicitar el rango de fechas
    print("Ingrese el rango de fechas para cancelar turnos.")
    fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
    fecha_fin = input("Fecha de fin (AAAA-MM-DD): ")

    # Validar las fechas
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido. Use el formato AAAA-MM-DD.")
        return

    if fecha_inicio > fecha_fin:
        print("La fecha de inicio no puede ser mayor que la fecha de fin.")
        return

    # Obtener las citas del médico en el rango de fechas
    sql = """
    SELECT cita.id_cita, paciente.nombre AS paciente_nombre, cita.fecha_cita, cita.hora_cita, cita.estado
    FROM cita
    JOIN paciente ON cita.id_paciente = paciente.id_paciente
    WHERE cita.id_medico = %s AND cita.fecha_cita BETWEEN %s AND %s
    """
    mycursor.execute(sql, (id_medico, fecha_inicio.date(), fecha_fin.date()))
    resultados = mycursor.fetchall()

    if not resultados:
        print(f"No se encontraron citas para el médico con ID {id_medico} en el rango de fechas proporcionado.")
        return

    print("Citas del médico en el rango de fechas:")
    # Mostrar las citas encontradas
    for turno in resultados:
        print(f"ID Cita: {turno[0]}, Paciente: {turno[1]}, Fecha: {turno[2]}, Hora: {turno[3]}, Estado: {turno[4]}")

    # Confirmación para proceder con la cancelación de todas las citas en el rango
    confirmar = input("¿Desea cancelar todas las citas en este rango de fechas? (s/n): ").lower()
    
    if confirmar == 's':
        # Proceder a cancelar las citas
        sql = "DELETE FROM cita WHERE id_medico = %s AND fecha_cita BETWEEN %s AND %s"
        try:
            mycursor.execute(sql, (id_medico, fecha_inicio.date(), fecha_fin.date()))
            mydb.commit()
            print(f"Se han cancelado todas las citas para el médico con ID {id_medico} en el rango de fechas proporcionado.")
        except mysql.connector.Error as err:
            print(f"Error al cancelar las citas: {err}")
    else:
        print("Cancelación de citas cancelada.")



# Función para ver los turnos de un paciente
def verTurnosPorPaciente(id_paciente):
    if not pacienteExiste(id_paciente):
        print(f"No se encontró un paciente con ID {id_paciente}.")
        return

    sql = "SELECT * FROM cita WHERE id_paciente = %s"
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
    if not medicoExiste(id_medico):
        print(f"No se encontró un médico con ID {id_medico}.")
        return

    sql = "SELECT * FROM cita WHERE id_medico = %s"
    mycursor.execute(sql, (id_medico,))
    resultados = mycursor.fetchall()
    if resultados:
        print("Turnos del médico:")
        for turno in resultados:
            print(f"ID Cita: {turno[0]}, Paciente ID: {turno[1]}, Fecha: {turno[3]}, Hora: {turno[4]}, Estado: {turno[5]}")
    else:
        print(f"No se encontraron turnos para el médico con ID {id_medico}.")


def reporte_mayores_turnos():
    """Genera un reporte con los 3 médicos que más turnos tienen."""
    
    try:
        # Consulta SQL para obtener los 3 médicos con más turnos
        mycursor.execute("""
            SELECT m.nombre, COUNT(*) AS cantidad_turnos
            FROM cita c
            JOIN Medico m ON c.id_medico = m.id_medico
            GROUP BY c.id_medico
            ORDER BY cantidad_turnos DESC
            LIMIT 3
        """)
        
        # Obtener los resultados
        resultados = mycursor.fetchall()
        
        # Verificar si se encontraron resultados
        if resultados:
            print("\nReporte de los 3 médicos con más turnos:")
            print("{:<20} {:<20}".format("Médico", "Cantidad de Turnos"))
            print("-" * 40)  # Imprimir una línea separadora
            
            # Mostrar los resultados
            for resultado in resultados:
                print("{:<20} {:<20}".format(resultado[0], resultado[1]))
        else:
            print("No se encontraron turnos registrados.")
    
    except Exception as e:
        print("Hubo un error al generar el reporte:", e)
