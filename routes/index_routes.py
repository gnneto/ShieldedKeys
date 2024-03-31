from flask import Blueprint, render_template, session, redirect, url_for
from models import Password

baseIndex = Blueprint('index', __name__)



@baseIndex.route('/listaSenhas')
def listarSenhas():
    passwords = Password.query.all()
    # verifica se o usuario esta logado
    if 'user_id' not in session:
        return redirect(url_for('acesso.login'))
    
    user_id = session['user_id']
    passwords = Password.query.filter_by(user_id=user_id).all()

    return render_template('sistema/lista_senhas.html', passwords=passwords, user_id=user_id)



@baseIndex.route('/')
def index():
    return render_template('index.html')

