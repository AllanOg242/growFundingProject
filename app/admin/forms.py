from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email


class AuthentiForm(FlaskForm):
    nom = StringField('Nom de la filiere', validators=[DataRequired()])
    code = IntegerField('code', validators=[DataRequired()])
    submit = SubmitField('Submit')
