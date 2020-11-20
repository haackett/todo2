from database import db
import datetime

class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, unique=False, nullable=False)
    completed = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    initialDate = db.Column(db.DateTime, default=datetime.date.today())

    @property
    def serialize(self):
        return {
            'text' : self.text,
            'completed' : self.completed,
        }

    def serialize_todo(todo):
        return {
            'id': todo.id,
            'text' : todo.text,
            'completed' : todo.completed,
        }