CREATE DATABASE Hospital;
USE Hospital;

CREATE TABLE Paciente (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    dni INT NOT NULL UNIQUE,
    genero ENUM('Masculino', 'Femenino', 'Otro') NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20) NOT NULL 
);

CREATE TABLE Medico (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE Cita (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha_cita DATE NOT NULL,
    hora_cita TIME NOT NULL,
    estado ENUM('Pendiente', 'Confirmada', 'Cancelada') DEFAULT 'Pendiente',
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    UNIQUE (id_medico, fecha_cita, hora_cita),
    UNIQUE (id_paciente, fecha_cita, hora_cita)
);

     
CREATE INDEX idx_especialidad ON Medico(especialidad);
CREATE INDEX idx_fecha_hora_cita ON Cita(fecha_cita, hora_cita);
CREATE INDEX idx_medico_paciente ON Cita(id_medico, id_paciente);
CREATE INDEX idx_nombre_paciente ON Paciente(dni);

