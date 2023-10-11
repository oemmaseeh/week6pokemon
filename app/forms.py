from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class pokemonform(FlaskForm):
    pokemon = StringField(label='pokemon name', validators = [DataRequired()])
    submit = SubmitField("search")