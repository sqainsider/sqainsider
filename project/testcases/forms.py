#forms.py

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField, SelectField, PasswordField
from wtforms.validators import DataRequired,Length, EqualTo
 
class TestScriptForm(Form):
	run=StringField("Run Status")
	case_id=StringField("case id", validators=[DataRequired()])
	seqnbr = StringField("case id", validators=[DataRequired()])
	status=StringField("case id", validators=[DataRequired()])
	page=StringField("Page Name", validators=[DataRequired()])
	label=StringField("label", validators=[DataRequired()])
	value=StringField("value", validators=[DataRequired()]) 
	elementid=StringField("element", validators=[DataRequired()])
	identifier = StringField("element", validators=[DataRequired()])
	method = StringField("element", validators=[DataRequired()])


	