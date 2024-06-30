/* DDL CON ENFOQUE EN SEGURIDAD*/
/* creamos un usuario con persimos solo para acceder a la base de datos db_blog*/
/* usuario: user1,  password: user-1 */
CREATE USER 'cac_user1'@'localhost' identified by 'cac_user-1';

GRANT ALL PRIVILEGES ON cac_noticias.* TO cac_user1@localhost;
FLUSH PRIVILEGES;
/*con esto eliminamos el usuario*/
DROP USER 'cac_user1'@'localhost';

/* DDL CON ENFOQUE EN SEGURIDAD*/