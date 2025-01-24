from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "clave_secreta"

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route("/ejercicio1", methods=["GET", "POST"])
def calculoCompras():
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        total_sin_descuento = cantidad_tarros * 9000

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15

        elif edad > 30:
            descuento = total_sin_descuento * 0.25

        else:
            descuento = 0


        total_pagar = total_sin_descuento - descuento

        return render_template('ejercicio1.html', nombre=nombre, edad=edad, cantidad_tarros=cantidad_tarros, total_sin_descuento=total_sin_descuento,
                           descuento=descuento, total_pagar=total_pagar)
    return render_template('ejercicio1.html')


@app.route("/ejercicio2", methods=["GET", "POST"])
def inicioSesion():
    mensaje = None
    if request.method == "POST":
        nombre1 = request.form["nombre1"]
        contrasena = request.form["contrasena"]

        if nombre1 in usuarios and usuarios[nombre1] == contrasena:
           if nombre1 == "juan":
                    mensaje = "Bienvenido administrador " + nombre1
           else:
                    mensaje = "Bienvenido usuario " + nombre1
        else:
                mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)


