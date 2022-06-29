from flask import Flask
app=Flask(__name__)

@app.route('/')

def rutaInicial():
    print('ingreso al enpoint inicial')
    return 'Bienvenido a tu primera API de CodiGo de Backend ;D'
app.run(debug=True)