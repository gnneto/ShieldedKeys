Guilherme Acacio Pinto Neto RA: 202302378935


# ShieldedKeys - Armazenamento seguro de senhas

# 1. Introdução

ShieldedKeys é um projeto em desenvolvimento baseado no framework Flask, com o objetivo de fornecer uma solução segura para gerenciar senhas. Ele permite que os usuários armazenem suas senhas no sistema, protegendo-as com hash no banco de dados. Para visualizar uma senha, o usuário precisa fornecer uma frase de segurança.

# 2. Funcionalidades Principais
- Cadastro de usuários.
- Cadastro e armazenamento seguro de senhas com hash no banco de dados.
- Visualização de senhas apenas com a frase de segurança correspondente.

# 3. Tecnologias Utilizadas
- Linguagem de Programação: Python
- Framework Web: Flask
- Banco de Dados: SQLite
- Frontend: HTML, CSS, Bootstrap, JavaScript
- Controle de Versão: Git
Vale ressaltar que, com o objetivo de simplificar testes e demais processos, o projeto está utilizando o banco de dados SQLite.

# 4. Crie e ative um ambiente virtual para isolar as dependências do projeto:

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

# 5. Configuração do Ambiente de Desenvolvimento
Siga os passos abaixo para configurar e executar o projeto:
1. Clone o repositório para sua máquina local. `https://github.com/gnneto/ShieldedKeys.git`
2. Configure o ambiente virtual e instale as dependências utilizando `pip install -r requirements.txt`.
3. Inicie o servidor de desenvolvimento com `python app.py`.


