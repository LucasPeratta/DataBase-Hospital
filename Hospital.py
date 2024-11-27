# hospital.py

# Importación de las funciones correspondientes de las vistas
from view.paciente_menu import gestionar_pacientes
from view.medico_menu import gestionar_medicos
from view.turnos_menu import gestionar_citas  # Controlador de turnos

def menu():
    while True:
        print("\n--- HOSPITAL ---")
        print("1. Paciente")
        print("2. Medico")
        print("3. Cita")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':  # Gestión de Pacientes
            gestionar_pacientes()  # Ahora gestionamos pacientes desde la vista

        elif opcion == '2':  # Gestión de Médicos
            gestionar_medicos()  # Ahora gestionamos médicos desde la vista

        elif opcion == '3':  # Gestión de Turnos
            gestionar_citas()  # Llamada al submenú de citas desde la vista

        elif opcion == '4':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
