from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email


class AuthentiForm(FlaskForm):
    nom = StringField('Nom de la filiere', validators=[DataRequired()])
    code = IntegerField('code', validators=[DataRequired()])
    submit = SubmitField('Submit')


class IndividuForm(FlaskForm):
    nom = StringField('Nom de lindividu', validators=[DataRequired()])
    prenom = StringField('Prenom de lindividu', validators=[DataRequired()])
    adresse = StringField('Adresse de lindividu', validators=[DataRequired()])
    telephone = StringField('Telephone de lindividu', validators=[DataRequired()])
    motif = StringField('Motif de lindividu', validators=[DataRequired()])
    somme = StringField('Somme de lindividu', validators=[DataRequired()])
    numCompte = StringField('NumCompte de lindividu', validators=[DataRequired()])
    submit = SubmitField('Ajouter')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
