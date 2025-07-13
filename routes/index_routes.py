from flask import Blueprint, render_template, session, redirect, url_for
from models import Password, User

baseIndex = Blueprint('index', __name__)



@baseIndex.route('/listaSenhas')
def listarSenhas():
    passwords = Password.query.all()
    # verifica se o usuario esta logado
    if 'user_id' not in session:
        return redirect(url_for('acesso.login'))
    
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    nome = user.nome if user else None

    user_logged = True if user_id else False
    passwords = Password.query.filter_by(user_id=user_id).all()

    return render_template('sistema/lista_senhas.html', passwords=passwords, user_logged=user_logged, nome=nome)



@baseIndex.route('/')
def index():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    nome = user.nome if user else None

    user_logged = True if user_id else False

    return render_template('index.html', nome=nome, user_logged=user_logged)

@baseIndex.route('/perfil')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('acesso.login'))
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    nome = user.nome if user else None

    user_logged = True if user_id else None
    creation_date_account = user.creation_date_account

    data_formatada = creation_date_account.strftime('%Y-%m-%d')
    
    return render_template('usuario/perfil.html', user=user, nome=nome, user_logged=user_logged, data_formatada=data_formatada)