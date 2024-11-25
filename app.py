from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de usuario (esto es solo para demostración, en una app real usarías una base de datos)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Guardar usuario en la lista
        users.append({'username': username, 'password': password})
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verificar si el usuario existe
        for user in users:
            if user['username'] == username and user['password'] == password:
                return f'Bienvenido, {username}!'
        return 'Credenciales incorrectas', 401
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
