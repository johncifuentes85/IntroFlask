from flask import Flask,render_template,jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect #llamamos el framework, se llama los tempplate para llamar la pagina
from flask_mysqldb import MySQL #lla,a la conexion a myslq


app = Flask(__name__)

#conexion a base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'agencia'

conexion = MySQL(app) # vinculo entre la aplicación y la bd

@app.route('/destinos')
def listar_destinos():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, destino, costo FROM viajes ORDER BY destino"
        cursor.execute(sql)
        destinos = cursor.fetchall()
        print(destinos)
        #data['mensaje'] = 'Exito'
        data['destinos'] = destinos
    except Exception as ex:    
            data['mensaje'] = 'Error ...'
    return jsonify(data) # recordar importar jsonify

#endpoint o rutas
@app.route('/')#la @ es un decorador y ('/') la ruta de la raiz y se crea una funcion que nos lleve la pagina 
#para poder que ejecute hay que parar el servidor con ctrl+c y vuelve y se ejecuta.
def index():
    return render_template('index.html') # ruta que nos lleva al index se debe importar la funcion y podemos agregarle los datos del diccionario


@app.route('/armaPlan')
def armaPlan():
    destinos = ['San Andres', 'Mexico', 'peru']
    return render_template('armaPlan.html', d = destinos)

def not_found(error):
    #return render_template("not_found.html"),404#para que lleve a la pagina error 
    return redirect(url_for('index'))#para que direcciones a index
app.register_error_handler(404,not_found) #para que ejecute la pagina si se da en una pagina que no existe

if __name__ == "__main__":
    app.run(debug=True, port=3200)#cambio el debug (para no tenerlo que detener para ver las modificaciones) y el puerto




