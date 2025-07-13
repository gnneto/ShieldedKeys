# ShieldedKeys - Armazenamento Seguro de Senhas

## Requisitos do Sistema
- Python 3.x [Você pode encontrar aqui](https://www.python.org/)
- Bibliotecas Python (especificadas no requirements.txt)

# Como Começar
#### Siga os passos abaixo para configurar e executar o projeto:

1. Crie e ative um ambiente virtual para isolar as dependências do projeto:
- **Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

- **Linux**
```sh
python -m venv venv
source venv/bin/activate
```

2. Clone o repositório para sua máquina local: `https://github.com/gnneto/shielded-keys.git`
3. Configure o ambiente virtual e instale as dependências utilizando `pip install -r requirements.txt`.
4. Inicie o servidor de desenvolvimento: `python app.py`.

Acesse o site na URL padrão em [http://127.0.0.1:5000](http://127.0.0.1:5000) *ou siga a URL informada no terminal.*


# Funcionalidades Principais
### Cadastro de Senhas
- **Cadastro e Armazenamento de Senhas**
  - Permite o armazenamento de novas senhas e dados de sistemas ou contas desejadas do usuário *(Nome do site, usuário, senha, frase de segurança, URL do site).*
- **Listegem de senha**
  - Apresenta uma lista de cards com os dados salvos do usuário. A senha somente será exibida mediante a frase de segurança correta sobre a respectiva senha.
- **Exclusão de Senhas**
  - Possibilita a exclusão de senhas.

### Relatório de Vazamentos de Dados
Com a utilização de um script em Python, é feita uma consulta na API do Have I Been Pwned, onde o objetivo é demonstrar os vazamentos de dados e utilizar como alerta para os usuários.
- **Listagem de Vazamentos**
  - É demonstrada uma listagem com as seguintes informações referentes aos vazamentos: ***Domínio, data da violação, dados comprometidos, quantidade comprometida, descrição.***

<br>

Tecnologias Utilizadas
- Linguagem de Programação: Python
- Framework Web: Flask
- Banco de Dados: SQLite
- Frontend: HTML, CSS, Bootstrap, JavaScript

Vale ressaltar que, com o objetivo de simplificar testes e demais processos, o projeto está utilizando o banco de dados SQLite.
