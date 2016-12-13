#forms.py

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField, SelectField, PasswordField
from wtforms.validators import DataRequired,Length, EqualTo
 

class AddTaskForm(Form):
	task_id = IntegerField()
	name = StringField('Task Name', validators=[DataRequired()])
	due_date = DateField('Date Due (mm/dd/yyyy)',
		validators = [DataRequired()], format = '%m/%d/%Y'
	)
	priority = SelectField('Priority',
		validators = [DataRequired()],
		choices= [
			('1','1'),('2','2'),('3','3'),('4','4'), ('5','5')
		]
	)
	status = IntegerField('Status')



class TestCaseForm(Form):
	run=StringField("Run Status")
	case_id=StringField("case id", validators=[DataRequired()])
	status=StringField("case id", validators=[DataRequired()])
	page=StringField("Page Name", validators=[DataRequired()])
	label=StringField("label", validators=[DataRequired()])
	value=StringField("value", validators=[DataRequired()]) 
	elementid=StringField("element", validators=[DataRequired()])
	identifier = StringField("element", validators=[DataRequired()])

	