from flask import Flask, render_template, request, redirect, url_for

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
    if request.method == 'POST':
        name = request.form['name']
        rg = request.form['rg']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmarsenha']

        # Validate the user input here
        # If the input is valid, create a new user account and redirect the user to the login page
        # If the input is invalid, render the registration page with an error message
        if validate_input(name, rg, email, password, confirm_password):
            create_user(name, rg, email, password)
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='Invalid input')

    return render_template('register.html')

def validate_input(name, rg, email, password, confirm_password):
    # Implement your input validation logic here
    # Return True if the input is valid, False otherwise
    pass

def create_user(name, rg, email, password):
    # Implement your user creation logic here
    # Create a new user account with the given name, rg, email, and password
    pass

if __name__ == '__main__':
    app.run(debug=True)






    
