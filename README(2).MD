# Proyecto Final - Base de Datos

_Universidad Tecnológica Nacional - Facultad Regional Bahía Blanca_  
_Materia:_ Base de Datos  
_Año:_ 2024

---

## Descripción del Proyecto

_Este proyecto consiste en:_

Diseñar e implementar una base de datos que permita:

- Registrar y gestionar la información de _pacientes_ (datos personales).
- Administrar los datos de _médicos_ (especialidad y contacto).
- Programar, buscar y cancelar _turnos médicos_.
- Generar _reportes de turnos_ para análisis y seguimiento.
- Realizar _búsquedas avanzadas_ para consultas específicas.

---

## Dependencias Funcionales (DFs)

| Dependencia Funcional    | Descripción                                            |
| ------------------------ | ------------------------------------------------------ |
| _id_paciente_            | Determina (nombre, edad, género, dirección, teléfono). |
| _id_medico_              | Determina (nombre, especialidad, teléfono).            |
| _id_cita_                | Determina (id_paciente, id_medico, fecha_cita).        |
| _id_paciente, id_medico_ | Determina (fecha_cita).                                |

---

## Claves Candidatas

| Tabla      | Clave Candidata                      |
| ---------- | ------------------------------------ |
| _Paciente_ | (id_paciente)                        |
| _Médico_   | (id_medico)                          |
| _Cita_     | (id_paciente, id_medico, fecha_cita) |

---

## Justificación del diseño:

_Primera Forma Normal (1NF):_
Regla: Cada columna debe contener valores atómicos (sin listas o conjuntos), y cada fila debe ser única.

Cumple, ya que:
Las columnas solo almacenan valores atómicos (un solo valor por celda).
Cada tabla tiene una clave primaria definida, garantizando filas únicas.

_Segunda Forma Normal (2NF):_
Regla: Debe estar en 1NF y no debe haber dependencias parciales (las columnas no clave dependen completamente de la clave primaria).

Cumple, ya que:
Todas las columnas dependen completamente de la clave primaria de sus respectivas tablas. Por ejemplo:
En Paciente, cada columna depende de id_paciente.
En Cita, id_paciente y id_medico son claves externas correctamente referenciadas.

_Tercera Forma Normal (3NF):_
Regla: Debe estar en 2NF y no debe haber dependencias transitivas (una columna no clave depende de otra columna no clave).

Cumple, ya que:
No hay dependencias transitivas en ninguna tabla. Todas las columnas no clave dependen directamente de la clave primaria.

_Nuevo diseño en la 3NF_

1. _Tabla Paciente_

   - id_paciente (Clave primaria)
   - nombre
   - edad
   - genero
   - direccion
   - telefono

2. _Tabla Medico_

   - id_medico (Clave primaria)
   - nombre
   - especialidad
   - telefono

3. _Tabla Cita_
   - id_cita
   - id_paciente (Clave foránea que referencia a Paciente)
   - id_medico (Clave foránea que referencia a Medico)
   - fecha_cita
   - hora_cita
   - Clave primaria compuesta: (id_paciente, id_medico, fecha_cita)

---

## ✨Objetivos

- Optimizar la gestión de información.
- Facilitar la programación y gestión de turnos.
- Implementar funcionalidades avanzadas.
- Simular un entorno realista.
- Mejorar habilidades técnicas.

---

## Capturas y Diagrama

---

## Autores

- _Belatti, Mateo Adaalberto_
- _Burgos, Belén_
- _Peratta, Lucas_
- _Robles, Gianfranco_

---

## Estado del Proyecto

- ✅ Diseño completado.
