# controller/turno_controller.py
from model.turnos_model import programarTurno, actualizarTurno, cancelarTurnoPorMedico, verTurnosPorPaciente, verTurnosPorMedico, reporte_mayores_turnos, cancelarTurnoPorFechas

# Función para manejar la creación de un turno
def programar_turno_controller(id_paciente, id_medico, fecha, hora):
    programarTurno(id_paciente, id_medico, fecha, hora)  # Llama a la función del modelo para crear el turno

# Función para manejar la actualización de un turno
def actualizar_turno_controller(id_cita, fecha=None, hora=None, estado=None):
    actualizarTurno(id_cita, fecha, hora, estado)  # Llama a la función del modelo para actualizar el turno

# Función para manejar la cancelación de un turno
def cancelar_turno_controller(id_medico):
    cancelarTurnoPorMedico(id_medico)  # Llama a la función del modelo para cancelar el turno

# Función para ver los turnos de un paciente
def ver_turnos_por_paciente_controller(id_paciente):
    verTurnosPorPaciente(id_paciente)  # Llama a la función del modelo para ver los turnos de un paciente

# Función para ver los turnos de un médico
def ver_turnos_por_medico_controller(id_medico):
    verTurnosPorMedico(id_medico)  # Llama a la función del modelo para ver los turnos de un médico

def reporte_mayores_turnos_controller():
    reporte_mayores_turnos()

def cancelar_turno_fecha_controller(id_medico):
    cancelarTurnoPorFechas(id_medico)
