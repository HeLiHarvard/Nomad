from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, FieldList
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, ValidationError

class AirportsForm(Form):
  places = FieldList(StringField('', validators=[DataRequired()]), min_entries=2)
  dates = FieldList(StringField('', validators=[DataRequired()]), min_entries=1)
