from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def land():
    return render_template('land.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # Here you can implement your login logic
    return f'Username: {username}, Password: {password}'
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # Here you can implement your login logic
    return f'Username: {username}, Password: {password}'




if __name__ == '__main__':
    app.run(debug=True)