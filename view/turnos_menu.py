# Importamos los controladores correspondientes para manejar las citas
from controllers.turno_controller import (
    programar_turno_controller,
    actualizar_turno_controller,
    cancelar_turno_controller,
    ver_turnos_por_paciente_controller,
    ver_turnos_por_medico_controller,
    reporte_mayores_turnos_controller,
    cancelar_turno_fecha_controller
)

def gestionar_citas():
    """Submenú para operaciones CRUD de citas."""
    while True:
        print("\n--- CITA ---")
        print("1. Nueva Cita")
        print("2. Modificar Cita")
        print("3. Cancelar Cita de Medico")
        print("4. Cancelar Citas de Medico por fechas")
        print("5. Ver citas por paciente")
        print("6. Ver citas por médico")
        print("7. Reporte de médicos con más turnos")
        print("8. Volver")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == '1':
            nueva_cita()
        elif sub_opcion == '2':
            modificar_cita()
        elif sub_opcion == '3':
            cancelar_cita()
        elif sub_opcion == '4':
            cancelar_citas_por_fecha()
        elif sub_opcion == '5':
            ver_citas_paciente()
        elif sub_opcion == '6':
            ver_citas_medico()
        elif sub_opcion == '7':
            reporte_mas_turno_por_medico()
        elif sub_opcion == '8':
            break
        else:
            print("Opción no válida.")

def nueva_cita():
    """Registrar una nueva cita."""
    id_paciente = input("ID del paciente: ")
    id_medico = input("ID del médico: ")
    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")
    # Llamamos al controlador para programar el turno
    programar_turno_controller(id_paciente, id_medico, fecha, hora)

def modificar_cita():
    """Modificar una cita existente."""
    id_cita = input("ID de la cita a modificar: ")
    fecha = input("Nueva fecha (opcional, AAAA-MM-DD): ")
    hora = input("Nueva hora (opcional, HH:MM:SS): ")
    estado = input("Nuevo estado ('Pendiente', 'Confirmada', 'Cancelada') or DEFAULT 'Pendiente'")
    # Llamamos al controlador para actualizar el turno
    actualizar_turno_controller(id_cita, fecha, hora, estado)

def cancelar_cita():
    """Cancelar una cita."""
    id_medico = input("ID del medico que tiene la cita a cancelar: ")
    # Llamamos al controlador para cancelar el turno
    cancelar_turno_controller(id_medico)

def cancelar_citas_por_fecha():
    """Cancelar citas por fecha."""
    id_medico = input("ID del medico que tiene la cita a cancelar: ")
    cancelar_turno_fecha_controller(id_medico)

def ver_citas_paciente():
    """Ver todas las citas de un paciente."""
    id_paciente = input("ID del paciente: ")
    # Llamamos al controlador para ver los turnos del paciente
    ver_turnos_por_paciente_controller(id_paciente)

def ver_citas_medico():
    """Ver todas las citas de un médico."""
    id_medico = input("ID del médico: ")
    # Llamamos al controlador para ver los turnos del médico
    ver_turnos_por_medico_controller(id_medico)

def reporte_mas_turno_por_medico():
    """Mostrar el reporte de los 3 médicos con más turnos."""
    reporte_mayores_turnos_controller()
