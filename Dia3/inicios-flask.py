from flask import Flask
from datetime import datetime
from flask_cors import CORS
app=Flask(__name__)

CORS(app)

@app.route('/')

def rutaInicial():
    print('ingreso al enpoint inicial')
    return 'Bienvenido a tu primera API de CodiGo de Backend ;D'
@app.route('/estado')
def estadoAPI():
    return{
        'hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
app.run(debug=True)