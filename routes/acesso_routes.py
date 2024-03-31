from flask import Blueprint, render_template, request, redirect, url_for, session
import bcrypt
from models import db, User
from datetime import datetime


acessoRoutes = Blueprint('acesso', __name__)

@acessoRoutes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        data_aniversario = datetime.strptime(request.form['data_aniversario'], '%Y-%m-%d').date()
        numero_telefone = request.form['numero_telefone']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        new_user = User(username=username, password_hash=hashed_password.decode('utf-8'), nome=nome, sobrenome=sobrenome, email=email, data_aniversario=data_aniversario, numero_telefone=numero_telefone)
        db.session.add(new_user)
        db.session.commit()

        return render_template('index.html')
    return render_template('usuario/cadastro.html')



@acessoRoutes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            session['user_id'] = user.id
            return render_template('index.html')
        else:
            error_message = "E-mail ou senha incorretos."
            return render_template('usuario/login.html', error_message=error_message)
    else:
        return render_template('usuario/login.html', error_message=None)
        
@acessoRoutes.route('/logout')
def logout():
    session.clear()
    return render_template('usuario/login.html')