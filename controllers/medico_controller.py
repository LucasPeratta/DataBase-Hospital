from model.medico_model import registrar_medico, actualizar_medico, eliminar_medico, buscar_medico_por_nombre, obtener_todos_los_medicos

#Función para manejar el registro de un médico
def registrar_medico_controller(nombre, especialidad, telefono):
    registrar_medico(nombre, especialidad, telefono)
    print(f"Médico {nombre} registrado correctamente.")

#Función para manejar la actualización de un médico
def actualizar_medico_controller(id_medico, nombre=None, especialidad=None, telefono=None):
    actualizar_medico(id_medico, nombre, especialidad, telefono)
    print(f"Médico con ID {id_medico} actualizado correctamente.")

#Función para manejar la eliminación de un médico
def eliminar_medico_controller(id_medico):
    eliminar_medico(id_medico)
    print(f"Médico con ID {id_medico} eliminado correctamente.")

#Función para manejar la búsqueda de un médico por nombre
def buscar_medico_por_nombre_controller(nombre):
    resultados = buscar_medico_por_nombre(nombre)
    if resultados:
        for medico in resultados:
            print(f"ID: {medico['id_medico']}, Nombre: {medico['nombre']}, Especialidad: {medico['especialidad']}, Teléfono: {medico['telefono']}")
    else:
        print(f"No se encontraron médicos con el nombre {nombre}.")

#Función para manejar la visualización de todos los médicos
def ver_medico_controller():
    resultados = obtener_todos_los_medicos()
    if resultados:
        for medico in resultados:
            print(f"ID: {medico['id_medico']}, Nombre: {medico['nombre']}, Especialidad: {medico['especialidad']}, Teléfono: {medico['telefono']}")
    else:
        print("No hay médicos registrados.")