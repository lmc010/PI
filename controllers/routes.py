from flask import redirect, render_template, request, url_for


def init_app(app):
    @app.route('/')
    def home():
        return render_template('Home.html')

    @app.route('/video')
    def video():
        return render_template('Video.html')
 
    @app.route('/perfil')
    def perfil():
        return render_template('Perfil.html')
    
    @app.route('/login')
    def login():
        return render_template('Login.html')
    
    @app.route('/loading')
    def loading():
        return render_template('Loading.html')
    
    @app.route('/editar')
    def editar():
        return render_template('Editar.html')
    
    @app.route('/curso')
    def curso():
        return render_template('Curso.html')
    
    @app.route('/cadastro')
    def cadastro():
        return render_template('Cadastro.html')
    
    
  