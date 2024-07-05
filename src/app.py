#importamos el modulo de flask para que funcione el proyecto
from flask import Flask, render_template, request, redirect, url_for

#importamos el modulo os para acceder mas facil a los directorios
import os

#Nos permitirá darle el nombre a la foto
from datetime import datetime 

# importamos para la base de datos
import database as db

#definimos la ruta absoluta del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#unimos las rutas de las carpetas src y templates a la ruta del proyecto de la línea anterior
template_dir = os.path.join(template_dir, 'src', 'templates')

#indicamos que se busque el archivo index.html (en carpeta templates) al lanzar la aplicación
app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
# @app.route('/') es un decorador que vincula una función con una URL específica del sitio web. En este caso, '/' representa la ruta raíz o homepage del sitio web.

# La función home() que sigue al decorador es la que se ejecutará cuando un usuario visite la página principal (homepage) del sitio. La declaración return render_template('index.html') dentro de esta función indica que Flask debe buscar y renderizar el archivo HTML llamado index.html, que generalmente contiene el contenido que se mostrará en la página principal del sitio web.

# IMPORTANTE: importar en la linea 2 del codigo el modulo render_template para lanzar la pagina index.html. Debe quedar asi:
# from flask import Flask, render_template


# cursor es un objeto que apunta a la base de datos y nos permitira interactuar con el. database es el nombre de la variable que se encuentra en el archivo database.py y que contiene toda la informacion de conexion a la base de datos.

#  cursor.execute("SELECT * FROM users") ejecuta la consulta sql a la base de datos

# el metodo fetchall toma todos los registros devueltos en la ejecucion de la consulta anterior y guarda el resultado en la variable miResultado.

# insertarObjectos = [] crea una lista vacia

# nombreDeColumnas = [columna[0] for columna in cursor.description]
# Los nombres de las columnas se obtienen de cursor.description y los guarda en la variable nombreDeColumnas.

# for unRegistro in miResultado:
#     insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
# Recorre cada registro del resultado de ejecutar la consulta y lo convierten en un diccionario. Esto se hace mediante el uso de zip() para emparejar los nombres de las columnas con los valores de cada registro. 

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM articulo")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()

    ############### LISTA LIMITADA PARA POSTRAR ###############
    cursor2 = db.database.cursor()
    cursor2.execute("SELECT * FROM articulo ORDER BY id DESC limit 3;")
    miResultado2 = cursor2.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos2 = [] 
    nombreDeColumnas2 = [columna[0] for columna in cursor2.description]
    
    for unRegistro in miResultado2:
        insertarObjectos2.append(dict(zip(nombreDeColumnas2, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor2.close()
    ############### LISTA LIMITADA PARA POSTRAR ###############
 
    return render_template('index.html', data=insertarObjectos, data2=insertarObjectos2)


# #Ruta para guardar usuarios en la bdd
# @app.route('/usuario', methods=['POST'])
# def addUser():
#     nombre = request.form['nombre']
#     apellido = 'ApellidoDefault'
#     email = 'email_default@default.com'
#     username = request.form['username']
#     contrasena = request.form['contrasena']
    

#     if username and nombre and contrasena:
#         cursor = db.database.cursor()
#         sql = "INSERT INTO usuario (nombre, apellido, email, username, contrasena) VALUES (%s, %s, %s, %s, %s)"
#         data = (nombre, apellido, email, username, contrasena)
#         cursor.execute(sql, data)
#         db.database.commit()
#     return redirect(url_for('home'))


# @app.route('/eliminar/<string:id>')
# def eliminar(id):
#     cursor = db.database.cursor()
#     sql = "DELETE FROM usuario WHERE id = %s"
#     data = (id,)
#     cursor.execute(sql, data)
#     db.database.commit()
#     return redirect(url_for('home'))

# @app.route('/editar/<string:id>', methods=['POST'])
# def edit(id):
#     nombre = request.form['nombre']
#     username = request.form['username']
#     contrasena = request.form['contrasena']

#     if nombre and username and contrasena:
#         cursor = db.database.cursor()
#         sql = "UPDATE usuario SET nombre = %s, username = %s, contrasena = %s WHERE id = %s"
#         data = (nombre, username, contrasena, id)
#         cursor.execute(sql, data)
#         db.database.commit()
#     return redirect(url_for('home'))
@app.route('/listado_interno')
def listado_interno():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM articulo ORDER BY id DESC")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('listado_interno.html', data=insertarObjectos)

######################### INICIO CRUD DE NOTICIAS #########################
@app.route('/carga')
def carga():
    return render_template('carga.html')
#Ruta para guardar usuarios en la bdd
######################### CARGA DE NOTICIAS #########################
@app.route('/articulo_art', methods=['POST'])
def articulo_art():
    ##################
    now= datetime.now()
    tiempo= now.strftime("%Y%H%M%S") #Años horas minutos y segundos
    ##################

    titulo = request.form['titulo']
    texto_articulo = request.form['texto_articulo']
    foto = request.files['imagen']
    
    if foto.filename!='':
        nuevoNombreFoto = tiempo+foto.filename #Concatena el nombre
        foto.save("../src/static/media/noticias/img/"+ nuevoNombreFoto) #Lo guarda en la carpeta
        # redefinimos la ruta para guardar
        ruta_nuevoNombreFoto = "media/noticias/img/"+ nuevoNombreFoto

    if titulo and texto_articulo and foto:
        cursor = db.database.cursor()
        sql = "INSERT INTO articulo (titulo, texto_articulo, imagen) VALUES (%s, %s, %s)"
        data = (titulo, texto_articulo,ruta_nuevoNombreFoto)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_interno'))
######################### ELIMINACION DE NOTICIAS #########################
@app.route('/eliminar_art/<string:id>')
def eliminar_art(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM articulo WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('listado_interno'))
######################### EDICION DE NOTICIAS #########################
@app.route('/editar_art/<string:id>', methods=['POST'])
def edit_art(id):
    ##################
    now= datetime.now()
    tiempo= now.strftime("%Y%H%M%S") #Años horas minutos y segundos
    ##################
    titulo = request.form['titulo']
    texto_articulo = request.form['texto_articulo']
    foto = request.files['imagen']

    imagen_anterior = request.form['imagen_anterior']
    
    if foto.filename!='':
        # print("entro por aca1")
        nuevoNombreFoto=tiempo+foto.filename #Concatena el nombre
        foto.save("../src/static/media/noticias/img/"+nuevoNombreFoto) #Lo guarda en la carpeta
        # redefinimos la ruta para guardar
        ruta_nuevoNombreFoto = "media/noticias/img/"+ nuevoNombreFoto

    elif foto.filename == '':
        foto = True
        ruta_nuevoNombreFoto = imagen_anterior
        # print("entro por aca 2")

    if titulo and texto_articulo and foto:
        # print("entro por aca 3")
        cursor = db.database.cursor()
        sql = "UPDATE articulo SET titulo = %s, texto_articulo = %s, imagen = %s WHERE id = %s"
        data = (titulo, texto_articulo,ruta_nuevoNombreFoto, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('listado_interno'))
######################### FINDE CRUD DE NOTICIAS #########################

######################### INICIO DE CONTACTO #########################
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
######################### FORMULARIO DE CONTACTO #########################
@app.route('/solicitud_contacto', methods=['POST'])
def solicitud_contacto():

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    comentario = request.form['comentario']

    if nombre and apellido and email and comentario:
        cursor = db.database.cursor()
        sql = "INSERT INTO contacto (nombre, apellido, email, comentario) VALUES (%s, %s, %s, %s)"
        data = (nombre, apellido, email, comentario)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('contacto'))
######################### LISTA DE CONTACTO #########################
@app.route('/listado_interno_contactos')
def listado_interno_contactos():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM contacto")
    miResultado = cursor.fetchall()
    
    #Convertir los datos a diccionario
    insertarObjectos = [] 
    nombreDeColumnas = [columna[0] for columna in cursor.description]
    
    for unRegistro in miResultado:
        insertarObjectos.append(dict(zip(nombreDeColumnas, unRegistro)))
    
    # Cierra el cursor para liberar recursos de memoria.    
    cursor.close()
    
    return render_template('listado_interno_contactos.html', data=insertarObjectos)
######################### ELIMINACION DE CONTACTO #########################
@app.route('/eliminar_solicitud_contacto/<string:id>')
def eliminar_solicitud_contacto(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM contacto WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('listado_interno_contactos'))
######################### FIN DE CONTACTO #########################

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')



    #ejecucion directa de este archivo en modo de desarrollador en el puerto 4000 del localhost o servidor local creado por flask.
if __name__ == '__main__':
    app.run(debug=True, port=4000)
