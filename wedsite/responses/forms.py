from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional, InputRequired, ValidationError
from wedsite.models import Response

class RegistrationForm(FlaskForm):
    username = StringField('Nome', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Cognome', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    adults = IntegerField('Adulti', validators=[InputRequired(), NumberRange(0,10)])
    children = IntegerField('Bambini (fino ai 10 anni)', validators=[InputRequired(), NumberRange(0,10)])
    message = TextAreaField("Commenti", validators=[Optional()], render_kw={"placeholder": "Intolleranze, allergie, richieste particolari...", 'rows':3})
    accomodation = BooleanField('Ho bisogno di un alloggio', validators=[Optional()])
    submit = SubmitField("Invia")

    def validate_email(self, email):
        email = Response.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Questa e-mail e' gia' stata utilizzata!")