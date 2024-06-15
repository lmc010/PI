from flask import redirect, render_template, request, url_for
from flask import render_template, request, url_for, redirect, flash, session
from models.database import db, Usuario, Curso
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import Markup
import urllib
import json

userList = []
cursoList = []

def init_app(app):
    
    @app.before_request
    def check_auth():
        # Rotas que não precisam de autenticação
        routes = ['login', 'cadastro', 'home', 'perfil','curso','video','editar' ]

        # Se a rota atual não requer autenticação, permite o acesso
        if request.endpoint in routes or request.path.startswith('/static/'):
            return

        # Se o usuário não estiver autenticado, redireciona para a página de login
        if 'user_id' not in session:
            return redirect(url_for('home'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = Usuario.query.filter_by(email=email).first()
            
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.email
                nickname = user.email.split('@')
                flash(f'Login bem-sucedido! Bem-vindo {nickname[0]}!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Falha no login. Verifique seu nome de usuário e senha.', 'danger') 
        return render_template('login.html')
    
    @app.route('/logout', methods=['GET', 'POST'])
    def logout():
        session.clear()
        flash('Desconectado com sucesso!', 'warning')
        return redirect(url_for('home'))    
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            password = request.form['password']
            user = Usuario.query.filter_by(email=email).first()
            if user:
                msg = Markup("Usuário já cadastrado. Faça <a href='/login'>login</a>.")
                flash(msg, 'danger')
                return redirect(url_for('cadastro'))
            else:
           # print(email, password)
                hashed_password = generate_password_hash(password, method='scrypt')
                new_user = Usuario(email=email, password=hashed_password, nome=nome)
                db.session.add(new_user)
                db.session.commit()               
            flash('Registro realizado com sucesso! Faça login', 'success')
            return redirect(url_for('login'))        
        return render_template('cadastro.html')   
    
    @app.route('/editar', methods=['GET', 'POST'])
    def editar():
        user = Usuario.query.get_or_404()
        if request.method == 'POST':
            user.nome = request.form['nome']
            user.email = request.form['email']
            user.password = generate_password_hash(request.form['password'], method='scrypt')
            db.session.commit()
            flash('Usuário editado com sucesso!', 'success')
            return redirect(url_for('perfil'))
        return render_template('editar.html')
    
    @app.route('/cadCurso', methods=['GET', 'POST'])
    def cadCurso():
        if request.method == 'POST':
            nomeCurso = request.form['nomeCurso']
            descricao = request.form['descricao']
            cargaHoraria = request.form['cargaHoraria']
            valor = request.form['valor']
            new_curso = Curso(nomeCurso=nomeCurso, descricao=descricao, cargaHoraria=cargaHoraria, valor=valor)
            db.session.add(new_curso)
            db.session.commit()
            print(new_curso)
            flash('Curso cadastrado com sucesso!', 'success')
            return redirect(url_for('home'))        
        return render_template('cadCurso.html', curso=curso)
    
    @pp.route('/editCurso', methods=['GET', 'POST'])
    def editCurso():
        curso = Curso.query.get_or_404()
        if request.method == 'POST':
            curso.nomeCurso = request.form['nomeCurso']
            curso.descricao = request.form['descricao']
            curso.cargaHoraria = request.form['cargaHoraria']
            curso.valor = request.form['valor']
            db.session.commit()
            flash('Curso editado com sucesso!', 'success')
            return redirect(url_for('home'))
        return render_template('editCurso.html')
    
    @app.route('deletCurso')
    def deleteCurso():
        curso = Curso.query.get_or_404()
        db.session.delete(curso)
        db.session.commit()
        flash('Curso deletado com sucesso!', 'warning')
        return redirect(url_for('editCurso'))         
                  
                
    @app.route('/home')
    def home():
        return render_template('Home.html')
    
    @app.route('/video')
    def video():
        return render_template('Video.html')
 
    @app.route('/perfil')
    def perfil():
        return render_template('Perfil.html')
    
    
    @app.route('/loading')
    def loading():
        return render_template('Loading.html')   
     
    @app.route('/curso')
    def curso():
        return render_template('Curso.html')
    
    
    
  