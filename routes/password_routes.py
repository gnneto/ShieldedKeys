import base64
import bcrypt
from flask import Blueprint, request, redirect, url_for, flash, session, jsonify
from models import db, Password, User

passwordRoutes = Blueprint('password', __name__)

@passwordRoutes.route('/cadastrarSenha', methods=['POST'])
def cadastrarSenha():
    site_name = request.form['siteName']
    username = request.form['username']
    password_plain = request.form['password']
    security_phrase = request.form['securityPhrase']
    url = request.form['url']
    phrase_hash = bcrypt.hashpw(security_phrase.encode(), bcrypt.gensalt())
    
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    
    # teste de segurança das senhas
    # user_info = f"{user.numero_telefone}{user.password_hash}"
    telfone = user.numero_telefone
    senha_hash = user.password_hash
    password_base64 = base64.b64encode(password_plain.encode()).decode()
    combined_info = telfone + password_base64 + senha_hash
    combined_base64 = base64.b64encode(combined_info.encode()).decode()


    new_password = Password(
        site_name=site_name,
        username=username,
        password_hash=combined_base64,
        security_phrase=phrase_hash,
        url=url,
        user_id=user_id
    )

    db.session.add(new_password)
    db.session.commit()
    return redirect(url_for('index.listarSenhas'))

@passwordRoutes.route('/exibirSenha/<int:password_id>', methods=['POST'])
def exibirSenha(password_id):
    password = Password.query.get(password_id)
    security_phrase = request.form['securityPhrase']

    # verifica a frase
    if bcrypt.checkpw(security_phrase.encode(), password.security_phrase):
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        telefone = user.numero_telefone
        senha_hash = user.password_hash
        
        # teste de segurança das senhas
        password_hash = password.password_hash.replace(telefone, '').replace(senha_hash, '')
        # print('password_hash', password_hash)
        
        password_plain = base64.b64decode(password_hash.encode()).decode()
        # print('password_plain antes ', password_plain)

        password_plain = password_plain.replace(telefone, "").replace(senha_hash, "")
        # print('password_plain depois ', password_plain)
        senhaPura = base64.b64decode(password_plain)
        senhaP = senhaPura.decode('utf-8')
        # print(senhaPura)
        password_plain = senhaP
        return jsonify({'senha': password_plain})
    else:
        return jsonify({'mensagem': 'Frase de segurança incorreta'}), 403
    



@passwordRoutes.route('/editarSenha/<int:password_id>', methods=['POST'])
def editarSenha(password_id):
    password = Password.query.get(password_id)
    if password:
        site_name = request.form['siteName']
        username = request.form['username']
        password_plain = request.form['password']
        security_phrase = request.form['securityPhrase']
        url = request.form['url']
        phrase_hash = bcrypt.hashpw(security_phrase.encode(), bcrypt.gensalt())

        user_id = session.get('user_id')
        user = User.query.get(user_id)

        telefone = user.numero_telefone
        senha_hash = user.password_hash
        password_base64 = base64.b64encode(password_plain.encode()).decode()
        combined_info = telefone + password_base64 + senha_hash
        combined_base64 = base64.b64encode(combined_info.encode()).decode()

        password.site_name = site_name
        password.username = username
        password.password_hash = combined_base64
        password.security_phrase = phrase_hash
        password.url = url

        db.session.commit()
        return jsonify({'mensagem': 'Senha atualizada com sucesso'}), 200
    else:
        return jsonify({'mensagem': 'Senha não encontrada'}), 404




@passwordRoutes.route('/deletarSenha/<int:password_id>')
def deletarSenha(password_id):
    password = Password.query.get(password_id)
    if password:
        db.session.delete(password)
        db.session.commit()
    else:
        flash('Senha não encontrada', 'danger')
    return redirect(url_for('index.listarSenhas'))