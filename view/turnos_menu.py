# Importamos los controladores correspondientes para manejar las citas
from controllers.turno_controller import (
    programar_turno_controller,
    actualizar_turno_controller,
    cancelar_turno_controller,
    ver_turnos_por_paciente_controller,
    ver_turnos_por_medico_controller
)

def gestionar_citas():
    """Submenú para operaciones CRUD de citas."""
    while True:
        print("\n--- CITA ---")
        print("1. Nueva Cita")
        print("2. Modificar Cita")
        print("3. Cancelar Cita")
        print("4. Ver citas por paciente")
        print("5. Ver citas por médico")
        print("6. Volver")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == '1':
            nueva_cita()
        elif sub_opcion == '2':
            modificar_cita()
        elif sub_opcion == '3':
            cancelar_cita()
        elif sub_opcion == '4':
            ver_citas_paciente()
        elif sub_opcion == '5':
            ver_citas_medico()
        elif sub_opcion == '6':
            break
        else:
            print("Opción no válida.")

def nueva_cita():
    """Registrar una nueva cita."""
    id_paciente = input("ID del paciente: ")
    id_medico = input("ID del médico: ")
    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM:SS): ")
    # Llamamos al controlador para programar el turno
    programar_turno_controller(id_paciente, id_medico, fecha, hora)

def modificar_cita():
    """Modificar una cita existente."""
    id_cita = input("ID de la cita a modificar: ")
    fecha = input("Nueva fecha (opcional, AAAA-MM-DD): ")
    hora = input("Nueva hora (opcional, HH:MM:SS): ")
    estado = input("Nuevo estado (opcional): ")
    # Llamamos al controlador para actualizar el turno
    actualizar_turno_controller(id_cita, fecha, hora, estado)

def cancelar_cita():
    """Cancelar una cita."""
    id_cita = input("ID de la cita a cancelar: ")
    # Llamamos al controlador para cancelar el turno
    cancelar_turno_controller(id_cita)

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
