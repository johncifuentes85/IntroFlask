from flask import Flask,render_template,jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect #llamamos el framework, se llama los tempplate para llamar la pagina
from flask_mysqldb import MySQL #lla,a la conexion a myslq


app = Flask(__name__)

#conexion a base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

conexion = MySQL(app) # vinculo entre la aplicación y la bd

@app.route('/cars')
def listar_cars():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, marca, modelo, valor FROM car ORDER BY marca"
        cursor.execute(sql)
        cars = cursor.fetchall()
        print(cars)
        data['mensaje'] = 'Exito'
        data['cars'] = cars
    except Exception as ex:    
            data['mensaje'] = 'Error ...'
    return jsonify(data) # recordar importar jsonify

#endpoint o rutas
@app.route('/')#la @ es un decorador y ('/') la ruta de la raiz y se crea una funcion que nos lleve la pagina 
#para poder que ejecute hay que parar el servidor con ctrl+c y vuelve y se ejecuta.
def index():
    #return "<h1> Hola, desde la pagina de inicio </h1>" #se puede pintar las etiquetas desde aca 
    vehiculos = ['Mazda', 'Chevrolet', 'Renault', 'Audi']
    datosindex = {
        'titulo':'Sistema de prueba',
        'subtitulo':'Bienvenido al sistema usuario: ',
        'vehiculos':vehiculos,
        'usuario':'usuarioprueba',
        'referencias':['2','Aveo','Logan', '5 power', 'Airton'],
        'modelo':['2020','2000','2021', '2015', '2018'],
        'catvehiculos': len(vehiculos)
    }
    return render_template('index.html', datos = datosindex) # ruta que nos lleva al index se debe importar la funcion y podemos agregarle los datos del diccionario
    
@app.route('/login')
def login():
    return render_template('login.html')

def not_found(error):
    #return render_template("not_found.html"),404#para que lleve a la pagina error 
    return redirect(url_for('index'))#para que direcciones a index
app.register_error_handler(404,not_found) #para que ejecute la pagina si se da en una pagina que no existe

if __name__ == "__main__":
    app.run(debug=True, port=3200)#cambio el debug (para no tenerlo que detener para ver las modificaciones) y el puerto




