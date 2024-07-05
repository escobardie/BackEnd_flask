/*		Elimina, si existe, la base de datos llamada cac_noticias 	*/
DROP DATABASE IF EXISTS cac_noticias;

/* 		Crea, si no existe, la base de datos llamada cac_noticias 	*/
CREATE DATABASE IF NOT EXISTS cac_noticias;

/* 		Selecciona la base de datos llamada cac_noticias	*/
USE cac_noticias;

/* 		Muestra las tablas de la base de datos seleccionada		*/
SHOW TABLES;

CREATE TABLE IF NOT EXISTS usuario (
	id INT UNSIGNED AUTO_INCREMENT,
	nombre VARCHAR(60) NOT NULL,
	apellido VARCHAR(60) NOT NULL,
	email VARCHAR(60) NOT NULL,
	username VARCHAR(30) NOT NULL,
	contrasena VARCHAR(30) NOT NULL,
	fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);
SELECT * FROM usuario;

CREATE TABLE IF NOT EXISTS articulo (
	id INT UNSIGNED AUTO_INCREMENT,
    ##id_usuario INT UNSIGNED NOT NULL,
    titulo varchar(45) NOT NULL,
    texto_articulo varchar(250) NOT NULL,
    imagen varchar(200) NOT NULL,
    PRIMARY KEY(id)
    #FOREIGN KEY(id_usuario) REFERENCES usuario(id)
);

CREATE TABLE IF NOT EXISTS contacto (
	id INT UNSIGNED AUTO_INCREMENT,
    nombre varchar(45) NOT NULL,
    apellido varchar(45) NOT NULL,
    email varchar(45) NOT NULL,
    comentario varchar(250) NOT NULL,
    PRIMARY KEY(id)
);




DROP TABLE articulo;

ALTER TABLE articulo
ADD COLUMN texto_articulo varchar(250) NOT NULL;

DESCRIBE articulo;

ALTER TABLE articulo
ADD COLUMN titulo varchar(45) NOT NULL;

DESCRIBE articulo;