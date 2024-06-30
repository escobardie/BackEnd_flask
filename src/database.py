import mysql.connector


database = mysql.connector.connect(
    host='localhost',
    user='cac_user1',
    password='cac_user-1',
    database='cac_noticias'
)
