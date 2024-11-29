from model.medico_model import registrar_medico, actualizar_medico, eliminar_medico, buscar_medico_por_nombre, obtener_todos_los_medicos

#Función para manejar el registro de un médico
def registrar_medico_controller(nombre, especialidad, telefono):
    registrar_medico(nombre, especialidad, telefono)

#Función para manejar la actualización de un médico
def actualizar_medico_controller(id_medico, nombre=None, especialidad=None, telefono=None):
    actualizar_medico(id_medico, nombre, especialidad, telefono)

#Función para manejar la eliminación de un médico
def eliminar_medico_controller(id_medico):
    eliminar_medico(id_medico)

#Función para manejar la búsqueda de un médico por nombre
def buscar_medico_por_nombre_controller(nombre):
   buscar_medico_por_nombre(nombre)
   

#Función para manejar la visualización de todos los médicos
def ver_medico_controller():
    obtener_todos_los_medicos()