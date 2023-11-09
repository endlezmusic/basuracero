from flask import Flask, request, render_template

app = Flask(__name__)

# Base de datos ficticia para almacenar las notificaciones de desechos sólidos
notificaciones = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notificar_basura', methods=['POST'])
def notificar_basura():
    if request.method == 'POST':
        ubicacion = request.form.get('ubicacion')
        descripcion = request.form.get('descripcion')
        # Podrías agregar más campos según tus necesidades

        # Crear un diccionario con la información de la notificación
        notificacion = {
            'ubicacion': ubicacion,
            'descripcion': descripcion
        }

        # Agregar la notificación a la base de datos
        notificaciones.append(notificacion)

        # Redirigir al usuario a una página de confirmación o a donde desees
        return render_template('confirmacion.html', notificacion=notificacion)

    # Manejar otros métodos HTTP si es necesario
    return "Método HTTP no admitido"

if __name__ == '__main__':
    app.run(debug=True)
