-- registro > conjunto de datosias tablas pueden contener 1 o varios registros
-- en el lenguaje de bd siempre se coloca un punto y coma 
CREATE DATABASE prueba;
-- Sirve para indicar en que bd queremos trabajar
USE prueba;

CREATE table productos(
-- dato > un valor que por si solo no me da una buena referencia
-- las bd estan compuesta por 1 o varias tablas y var
-- obligatoriamente para crear una tabla debemos crear como minimo 1 columna
-- SOLAMENTE SE PUEDER USAR 1 VEZ EL AUTOINCREMENT POR TABLA
id INT auto_increment primary key,
NOMBRE varchar(50),
fecha_vencimiento DATE
);