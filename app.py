from flask import Flask, render_template
from routes.index_routes import baseIndex
from routes.acesso_routes import acessoRoutes
from routes.password_routes import passwordRoutes
from models import db

app = Flask(__name__)
app.secret_key = 'chaveSecreta'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skeys.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



# ROTAS BLUEPRINTS
app.register_blueprint(baseIndex)
app.register_blueprint(acessoRoutes)
app.register_blueprint(passwordRoutes)






with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)