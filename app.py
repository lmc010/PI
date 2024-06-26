from flask import Flask, render_template
from controllers import routes
import os
from models.database import db

app = Flask(__name__, template_folder='views')

routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/LibertyCursos.sqlite3')

# SECRET KEY FLASH MESSAGE
app.config['SECRET_KEY'] = 'libertysecret'

if __name__ == '__main__': 
    # Verifica no início da aplicação se o BD já existe. Caso contrário ele criará o BD.
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)
