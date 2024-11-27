from model.db_database import mycursor, mydb

def registrarPaciente(nombre, edad, dni, genero, direccion, telefono):
    try: 
        sql = "INSERT INTO Paciente (nombre, edad, dni, genero, direccion, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
        val = [(nombre, edad, dni, genero, direccion, telefono)]
        mycursor.executemany(sql, val)
        mydb.commit()
        print("-Paciente creado con exito-")
    except:
        print("\Error al crear paciente")


def mostrarTodos():
    mycursor.execute("SELECT * FROM Paciente")
    resultados = mycursor.fetchall()
    for registro in resultados:
        print(registro)  

def buscarPorDni(dni):
    mycursor.execute(f"SELECT * FROM Paciente WHERE dni = {dni}")
    resultado = mycursor.fetchone()
    print("La informacion del paciente es la siguiente")
    print(resultado)

def EliminarPaciente(id):
    sql = "DELETE FROM Paciente WHERE id_paciente = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registro(s) eliminado(s)")

def modificarPaciente(id, nombre, edad, dni, genero, direccion, telefono):
    try:
        sql = f"UPDATE Paciente SET nombre = {nombre}, edad = {edad}, dni = {dni}, genero = {genero}, direccion = {direccion}, telefono = {telefono} WHERE id_paciente = {id}"
        val = (nombre, edad, dni, genero, direccion, telefono)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "registro(s) actualizado(s)")
    except:
        print("\nHubo un error al modificar el paciente")
