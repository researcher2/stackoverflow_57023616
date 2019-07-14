from app import db

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tasks = db.relationship('Task', backref='survey', lazy='dynamic')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    assignments = db.relationship('Assignment', backref='task', lazy='dynamic')

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    responses = db.relationship('Response', backref='assignment', lazy='dynamic')

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'))
    response_item = db.Column(db.String(255))
    response_value = db.Column(db.String(255))