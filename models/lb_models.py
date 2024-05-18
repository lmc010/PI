from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

# Connect to the MongoDB database
mongo = PyMongo(app)

# Define the User model
class User(mongo.db.Document):
    name = mongo.db.StringField(required=True, max_length=50)
    rg = mongo.db.StringField(required=True, max_length=9)
    email = mongo.db.StringField(required=True, unique=True)
    password = mongo.db.StringField(required=True, max_length=50)
    confirm_password = mongo.db.StringField(required=True, max_length=50)

    def save_user(self, password):
        # Hash the password before saving it to the database
        self.password = generate_password_hash(password)
        self.confirm_password = None
        self.save()

    def check_password(self, password):
        # Check if the given password matches the user's hashed password
        return check_password_hash(self.password, password)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired(), Length(min=2, max=50)])
    rg = StringField('RG', validators=[DataRequired(), Length(min=9, max=9)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar-se')