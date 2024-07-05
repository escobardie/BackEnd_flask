USE cac_noticias;
SELECT * FROM usuario;

insert into usuario(nombre, apellido, email, username, contrasena) 
values('Juan','Perez','Juancito@hotmail.com','juanperez','1234');


insert into usuario(nombre, apellido, email, username, contrasena) 
values('Diego','Escobar','diegoesco@hotmail.com','escobardie','224514');

SELECT * FROM articulo;

INSERT INTO articulo (titulo, texto_articulo, imagen)
VALUES ('ULTIMO', 'ESTE ES EL ULTIMO', 'media/noticias/img/2024012030tenor (1).gif');

SELECT * FROM articulo ORDER BY id DESC limit 3;

INSERT INTO contacto (nombre, apellido, email, comentario)
VALUES ('diego', 'escobar', 'diego@diego.com', 'comentario para completar.');

SELECT * FROM contacto;