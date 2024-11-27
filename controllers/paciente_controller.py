# controller/paciente_controller.py
from model.paciente_model import registrarPaciente, modificarPaciente, EliminarPaciente, mostrarTodos, buscarPorDni

# Función para manejar la creación de un paciente
def registrar_paciente_controller(nombre, edad, dni, genero, direccion, telefono):
    registrarPaciente(nombre, edad, dni, genero, direccion, telefono)  # Llama a la función del modelo para registrar el paciente

# Función para manejar la modificación de un paciente
def modificar_paciente_controller(id_paciente, nombre, edad, dni, genero, direccion, telefono):
    modificarPaciente(id_paciente, nombre, edad, dni, genero, direccion, telefono)  # Llama a la función del modelo para modificar el paciente

# Función para manejar la eliminación de un paciente
def eliminar_paciente_controller(id_paciente):
    EliminarPaciente(id_paciente)  # Llama a la función del modelo para eliminar el paciente

# Función para ver todos los pacientes
def ver_todos_pacientes_controller():
    mostrarTodos()  # Llama a la función del modelo para ver todos los pacientes

# Función para buscar un paciente por su DNI
def buscar_paciente_por_dni_controller(dni):
    buscarPorDni(dni)  # Llama a la función del modelo para buscar el paciente por DNI
