from flask import Flask,render_template #llamamos el framework, se llama los tempplate para llamar la pagina

app = Flask(__name__)

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
        'catvehiculos': len(vehiculos)
    }
    return render_template('index.html', datos = datosindex) # ruta que nos lleva al index se debe importar la funcion y podemos agregarle los datos del diccionario
    
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True, port=3200)#cambio el debug (para no tenerlo que detener para ver las modificaciones) y el puerto




