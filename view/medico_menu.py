from controllers.medico_controller import registrar_medico_controller, actualizar_medico_controller, eliminar_medico_controller, buscar_medico_por_nombre_controller, ver_medico_controller

#Submenú para gestionar médicos
def gestionar_medicos():
    """Submenú para operaciones CRUD de médicos."""
    while True:
        print("\n--- MEDICO ---")
        print("1. Registrar Médico")
        print("2. Modificar Médico")
        print("3. Eliminar Médico")
        print("4. Buscar Médico por nombre")
        print("5. Ver todos los médicos")
        print("6. Volver")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == '1':
            registrar_medico()
        elif sub_opcion == '2':
            modificar_medico()
        elif sub_opcion == '3':
            eliminar_medico()
        elif sub_opcion == '4':
            buscar_medico_por_nombre()
        elif sub_opcion == '5':
            ver_todos_los_medicos()
        elif sub_opcion == '6':
            break  # Salir del submenú y volver al menú principal
        else:
            print("Opción no válida.")

def registrar_medico():
    """Función para registrar un nuevo médico."""
    nombre = input("Nombre del médico: ")
    especialidad = input("Especialidad del médico: ")
    telefono = input("Teléfono del médico: ")
    registrar_medico_controller(nombre, especialidad, telefono)

def modificar_medico():
    """Función para modificar los datos de un médico existente."""
    id_medico = int(input("ID del médico a modificar: "))
    nombre = input("Nuevo nombre (opcional): ")
    especialidad = input("Nueva especialidad (opcional): ")
    telefono = input("Nuevo teléfono (opcional): ")
    actualizar_medico_controller(id_medico, nombre, especialidad, telefono)

def eliminar_medico():
    """Función para eliminar un médico."""
    id_medico = int(input("ID del médico a eliminar: "))
    eliminar_medico_controller(id_medico)

def buscar_medico_por_nombre():
    """Función para buscar un médico por nombre."""
    nombre = input("Nombre del médico a buscar: ")
    buscar_medico_por_nombre_controller(nombre)

def ver_todos_los_medicos():
    """Función para ver todos los médicos."""
    ver_medico_controller()