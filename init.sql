CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15),
    direccion VARCHAR(255),
    fecha_registro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS facturas (
    id_factura SERIAL PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    fecha_emision TIMESTAMP DEFAULT NOW(),
    descripcion VARCHAR(255) NOT NULL,
    monto REAL NOT NULL CHECK (monto > 0),
    estado VARCHAR(10) CHECK (estado IN ('Pendiente', 'Pagada', 'Cancelada')) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
