USE Hospital;

INSERT INTO
    Paciente (
        nombre,
        edad,
        dni,
        genero,
        direccion,
        telefono
    )
VALUES (
        'Juan Pérez',
        45,
        12345678,
        'Masculino',
        'Av. Libertador 1234, CABA',
        '1123456789'
    ),
    (
        'María Gómez',
        32,
        87654321,
        'Femenino',
        'Calle Falsa 567, Buenos Aires',
        '1134567890'
    ),
    (
        'Carlos Martínez',
        28,
        23456789,
        'Masculino',
        'San Juan 234, Mendoza',
        '1145678901'
    ),
    (
        'Ana López',
        60,
        34567890,
        'Femenino',
        'Rivadavia 876, La Plata',
        '1156789012'
    ),
    (
        'Pedro Fernández',
        52,
        45678901,
        'Masculino',
        'Parque Centenario 456, Rosario',
        '1167890123'
    ),
    (
        'Lucía Romero',
        25,
        56789012,
        'Femenino',
        'Calle 25 de Mayo 234, Córdoba',
        '1178901234'
    ),
    (
        'Tomás González',
        38,
        67890123,
        'Masculino',
        'Av. 9 de Julio 1200, CABA',
        '1189012345'
    ),
    (
        'Sofía Martínez',
        40,
        78901234,
        'Femenino',
        'Belgrano 876, Santa Fe',
        '1190123456'
    ),
    (
        'Felipe Díaz',
        33,
        89012345,
        'Masculino',
        'San Martín 300, Tucumán',
        '1201234567'
    ),
    (
        'Valentina Pérez',
        27,
        90123456,
        'Femenino',
        'Bv. Chacabuco 435, Rosario',
        '1212345678'
    );

INSERT INTO
    Medico (
        nombre,
        especialidad,
        telefono
    )
VALUES (
        'Dr. José Rodríguez',
        'Cardiología',
        '1122334455'
    ),
    (
        'Dra. Laura Sánchez',
        'Pediatría',
        '1133445566'
    ),
    (
        'Dr. Andrés Pérez',
        'Ginecología',
        '1144556677'
    ),
    (
        'Dra. Marta Ruiz',
        'Dermatología',
        '1155667788'
    ),
    (
        'Dr. Luis Fernández',
        'Oftalmología',
        '1166778899'
    ),
    (
        'Dra. Isabel García',
        'Neurología',
        '1177889900'
    ),
    (
        'Dr. Jorge Martínez',
        'Traumatología',
        '1188990011'
    ),
    (
        'Dra. Ana Jiménez',
        'Odontología',
        '1199001122'
    ),
    (
        'Dr. Ricardo López',
        'Psiquiatría',
        '1200112233'
    ),
    (
        'Dra. Carla González',
        'Medicina General',
        '1211223344'
    );

INSERT INTO
    Cita (
        id_paciente,
        id_medico,
        fecha_cita,
        hora_cita,
        estado
    )
VALUES (
        1,
        1,
        '2024-11-30',
        '10:00:00',
        'Pendiente'
    ),
    (
        2,
        2,
        '2024-11-30',
        '11:00:00',
        'Confirmada'
    ),
    (
        3,
        3,
        '2024-11-30',
        '14:00:00',
        'Cancelada'
    ),
    (
        4,
        4,
        '2024-12-01',
        '09:00:00',
        'Pendiente'
    ),
    (
        5,
        5,
        '2024-12-01',
        '15:00:00',
        'Confirmada'
    ),
    (
        6,
        6,
        '2024-12-02',
        '08:30:00',
        'Pendiente'
    ),
    (
        7,
        7,
        '2024-12-02',
        '13:30:00',
        'Confirmada'
    ),
    (
        8,
        8,
        '2024-12-03',
        '10:30:00',
        'Pendiente'
    ),
    (
        9,
        9,
        '2024-12-03',
        '11:30:00',
        'Confirmada'
    ),
    (
        10,
        10,
        '2024-12-04',
        '16:00:00',
        'Pendiente'
    ),
    (
        1,
        2,
        '2024-12-05',
        '14:00:00',
        'Confirmada'
    ),
    (
        2,
        3,
        '2024-12-05',
        '09:00:00',
        'Pendiente'
    ),
    (
        3,
        4,
        '2024-12-06',
        '10:00:00',
        'Cancelada'
    ),
    (
        4,
        5,
        '2024-12-06',
        '12:00:00',
        'Pendiente'
    ),
    (
        5,
        6,
        '2024-12-07',
        '08:00:00',
        'Confirmada'
    );