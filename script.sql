-- Crear la base de datos
CREATE DATABASE gestor_tareas;

-- Usar la base de datos
USE gestor_tareas;

-- Crear la tabla de tareas
CREATE TABLE tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Identificador único para cada tarea
    titulo VARCHAR(255) NOT NULL,               -- Título de la tarea, obligatorio
    descripcion TEXT,                           -- Descripción de la tarea, opcional
    estado ENUM('pendiente', 'completada')      -- Estado de la tarea, valores limitados
        DEFAULT 'pendiente',                    -- Estado predeterminado: "pendiente"
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Fecha y hora de creación
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Fecha y hora de última actualización
);
