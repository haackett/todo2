from database import db
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, unique=False, nullable=False)
    completed = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    requesting_user = db.Column(db.String, unique=False, nullable=False, default='Website')
    dependent_users = db.Column(MutableList.as_mutable(PickleType), default=[])

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
            'requesting_user' : todo.requesting_user,
            'dependent_users' : todo.dependent_users,
        }
    
    def list_users(users):
        py_list_users = []
        for user in users:
            py_list_users.append(user)
        return py_list_users
