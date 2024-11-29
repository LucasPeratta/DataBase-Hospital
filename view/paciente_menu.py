# view/menu_paciente.py
from controllers.paciente_controller import registrar_paciente_controller, modificar_paciente_controller, buscar_paciente_por_dni_controller, eliminar_paciente_controller, ver_todos_pacientes_controller

def gestionar_pacientes():
    """Submenú para operaciones CRUD de pacientes."""
    while True:
        print("\n--- PACIENTE ---")
        print("1. Registrar Paciente")
        print("2. Modificar Paciente")
        print("3. Eliminar Paciente")
        print("4. Ver todos los pacientes")
        print("5. Buscar paciente por DNI")
        print("6. Volver")
        sub_opcion = input("Seleccione una opción: ")

        if sub_opcion == '1':
            registrar_paciente()
        elif sub_opcion == '2':
            modificar_paciente()
        elif sub_opcion == '3':
            eliminar_paciente()
        elif sub_opcion == '4':
            ver_todos_pacientes()
        elif sub_opcion == '5':
            buscar_paciente_por_dni()
        elif sub_opcion == '6':
            break
        else:
            print("Opción no válida.")

def registrar_paciente():
    """Registrar un nuevo paciente."""
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    dni = input("DNI: ")
    genero = input("Género(Masculino / Femenino / Otro): ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    registrar_paciente_controller(nombre, edad, dni, genero, direccion, telefono)

def modificar_paciente():
    """Modificar un paciente existente."""
    id_paciente = input("ID del paciente a modificar: ")
    nombre = input("Nuevo nombre: ")
    edad = input("Nueva edad: ")
    dni = input("Nuevo DNI: ")
    genero = input("Nuevo género(Masculino / Femenino / Otro): ")
    direccion = input("Nueva dirección: ")
    telefono = input("Nuevo teléfono: ")
    modificar_paciente_controller(id_paciente, nombre, edad, dni, genero, direccion, telefono)

def eliminar_paciente():
    """Eliminar un paciente por ID."""
    id_paciente = input("ID del paciente a eliminar: ")
    eliminar_paciente_controller(id_paciente)

def ver_todos_pacientes():
    """Ver todos los pacientes registrados."""
    ver_todos_pacientes_controller()

def buscar_paciente_por_dni():
    """Buscar un paciente por su DNI."""
    dni = input("DNI del paciente a buscar: ")
    buscar_paciente_por_dni_controller(dni)
