# Importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Carregando o SQLAlchemy na variável DB
db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password
        
class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeCurso = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.String(100), nullable=False)
    cargaHoraria = db.Column(db.String(100), nullable=False)
    
    def __init__(self, nomeCurso, descricao, valor, cargaHoraria):
        self.nomeCurso = nomeCurso
        self.descricao = descricao
        self.valor = valor
        self.cargaHoraria = cargaHoraria