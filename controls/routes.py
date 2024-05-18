from flask import Flask, render_template, request, redirect, url_for
from models.lb_models import User, RegistrationForm

app = Flask(__name__)

@app.route('/home')

def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Validate the user credentials here
        # If the credentials are valid, redirect the user to the home page
        # If the credentials are invalid, render the login page with an error message
        if validate_user(email, password):
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')

def validate_user(email, password):
    # Implement your user validation logic here
    # Return True if the user is valid, False otherwise
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new user account with the form data
        user = User(name=form.name.data, rg=form.rg.data, email=form.email.data)
        user.save_user(form.password.data)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

def validate_input(name, rg, email, password, confirm_password):
    # Implement your input validation logic here
    # Return True if the input is valid, False otherwise
    pass

def create_user(name, rg, email, password):
    # Implement your user creation logic here
    # Create a new user account with the given name, rg, email, and password
    pass

@app.route('/logout')
def logout():
    return redirect('login')

@app.route('/video')

def video():
    return render_template('video.html')

@app.route('/curso')

def curso():
    return render_template('curso.html')

if __name__ == '__main__':
    app.run(debug=True)






    
