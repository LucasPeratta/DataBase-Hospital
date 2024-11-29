# Proyecto de Gestión de Hospital

Este proyecto es una aplicación de gestión de hospital que interactúa con una base de datos MySQL. Permite gestionar pacientes, médicos, turnos y más. A continuación, se proporcionan las instrucciones para clonar y ejecutar el proyecto.

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos instalados:

- **Python 3.7 o superior**
- **MySQL** (o MariaDB) instalado en tu máquina
- **Librería MySQL Connector para Python** (si no la tienes instalada, ejecuta el siguiente comando):

  ```bash
  pip install mysql-connector-python

  ```

- **Luego** debera conectarse a la base de datos utilizando:
  mysql -u root -p
  Y luego su contraseña que es "root" por determiando. (la puede cambiar en el archivo init_db.py)

- **LUEGO** usar comandos:
  python init_db.py
  python Hospital.py