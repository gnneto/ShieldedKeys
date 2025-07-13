from flask import Blueprint, render_template, session, redirect, url_for
from models import User
import requests

vazamentosRoutes = Blueprint('leak', __name__)

@vazamentosRoutes.route('/vazamentos')
def vazamentos():
    # verifica se o usuario esta logado
    if 'user_id' not in session:
        return redirect(url_for('acesso.login'))
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    nome = user.nome if user else None

    # coleta de dados vazados
    url = 'https://haveibeenpwned.com/api/v3/breaches'
    conct = requests.get(url)
    dados = conct.json()

    dadosFormatados = []
    for linha in dados:
        dadosLinha = {
            "Nome": linha['Name'],
            "Dominio": linha['Domain'],
            "Data da Violacao": linha['BreachDate'],
            "Contas comprometidas": linha['PwnCount'],
            "Dados comprometidos": ', '.join(linha['DataClasses']),
            "Descricao": linha['Description']
        }
        dadosFormatados.append(dadosLinha)

    user_logged = True if user_id else False
    return render_template('sistema/vazamentos.html', dados=dadosFormatados, user_logged=user_logged, nome=nome)