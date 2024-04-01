from flask import Blueprint, request, redirect, url_for, flash, session, jsonify
from models import db, Password
import bcrypt

passwordRoutes = Blueprint('password', __name__)

@passwordRoutes.route('/cadastrarSenha', methods=['POST'])
def cadastrarSenha():
    
    site_name = request.form['siteName']
    username = request.form['username']
    password_hash = request.form['password']
    security_phrase = request.form['securityPhrase']
    url = request.form['url']
    
    
    user_id = session.get('user_id')

    hashed_password = bcrypt.hashpw(password_hash.encode('utf-8'), bcrypt.gensalt())
    
    new_password = Password(
        site_name=site_name,
        username=username,
        password_hash=hashed_password,
        security_phrase=security_phrase,
        url=url,
        user_id=user_id
    )

    db.session.add(new_password)
    db.session.commit()
    return redirect(url_for('index.listarSenhas'))

@passwordRoutes.route('/exibirSenha/<int:password_hash>', methods=['POST'])
def exibirSenha(password_hash):
    password = Password.query.get(password_hash)
    security_phrase = request.form['securityPhrase']

    if password.check_security_phrase(security_phrase):
        return jsonify({'senha': password.password_hash.decode('utf-8')})
    else:
        return jsonify({'mensagem': 'Frase de segurança incorreta'}), 403
