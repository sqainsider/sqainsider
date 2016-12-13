#models.py


from project import db
from datetime import datetime


class Task(db.Model):

	__tablename__ = "tasks"

	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	due_date = db.Column(db.Date, nullable=False)
	priority = db.Column(db.Integer, nullable=False)
	posted_date = db.Column(db.Date, default= datetime.utcnow())
	status = db.Column(db.Integer)
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


	def __init__(self, name, due_date, priority, posted_date, status,user_id):
			self.name = name
			self.due_date = due_date
			self.priority = priority
			self.posted_date = posted_date
			self.status = status
			self.user_id = user_id

	def _repr__(self):
		return '<name {0}>' .format(self.name)


class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)
	role = db.Column(db.String, default='user')
	tasks = db.relationship('Task', backref='poster')
	
	def __init__(self, name=None, email=None, password=None, role=None):
			self.name = name
			self.email = email
			self.password = password
			self.role = role
			
	
	def _repr__(self):
		return '<name {0}>' .format(self.name)


class step(db.Model):

	__tablename__ = "steps"

	id = db.Column(db.Integer, primary_key=True)
	run = db.Column(db.String, nullable=True)
	caseid = db.Column(db.String, nullable=True)
	seqno = db.Column(db.String, nullable=True)
	status = db.Column(db.String, nullable=True)
	page = db.Column(db.String, nullable=True)
	label = db.Column(db.String, nullable=True)
	value = db.Column(db.String, nullable=True)
	verifications = db.Column(db.String, nullable=True)
	conditions = db.Column(db.String, nullable=True)
	comments = db.Column(db.String, nullable=True)
	elementid = db.Column(db.String, nullable=True)
	identifier = db.Column(db.String, nullable=True)
	method = db.Column(db.String, nullable=True)
	action = db.Column(db.String, nullable=True)
	

	def __init__(self, run=None, caseid=None, seqno=None, status=None, page=page,label=label, value =value, 
		verifications= verifications, conditions=conditions, comments =comments,
		elementid=elementid,identifier=identifier,method = method, action=action):
			self.run=None, 
			self.caseid=None, 
			self.seqno=None, 
			self.status=None, 
			self.page=page,
			self.label=label, 
			self.value =value, 
			self.verifications= verifications, 
			self.conditions=conditions, 
			self.comments =comments,
			self.elementid=elementid,
			self.identifier=identifier,
			self.method = method, 
			self.action=action


	
	def _repr__(self):
		return '<name {0}>' .format(self.name)

