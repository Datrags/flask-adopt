from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet species")
    photo_url = StringField("Photo URL", validators=[Optional(), 
                                                     URL(message="Invalid URL")])
    age = IntegerField("Age", validators=[InputRequired(), 
                                          NumberRange(0, 30, "Invalid Age")
                                        ])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available?")