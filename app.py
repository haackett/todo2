import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import database
import commands
from model import Todo

app = Flask(__name__, static_folder='client/todo/build/', static_url_path='/')
app.config.from_object(os.environ['APP_SETTINGS'])
CORS(app)

ADMIN = '<@149333543191838720>'

# setup dependencies
database.init_app(app)
commands.init_app(app)

@app.route("/")
def main_page():
    return send_from_directory(app.static_folder,'index.html')


"""
API METHODS
"""

@app.route('/todos/', methods=['GET'])
def get_todos():
    response = jsonify([*map(Todo.serialize_todo, database.db.session.query(Todo).all())])
    return response

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    response = jsonify(Todo.serialize_todo(todo))
    return response

@app.route('/todos/', methods=['POST'])
def add_todo():
    post_data = request.get_json()
    text = post_data.get("text")
    requesting_user = post_data.get("requesting_user")
    dependent_users = post_data.get("dependent_users")
    todo = Todo(text=text, requesting_user=requesting_user, dependent_users=dependent_users)
    database.db.session.add(todo)
    database.db.session.commit()
    print("Commiting Todo: " + str(Todo.serialize_todo(todo)))
    response = jsonify({'success' : True}, Todo.serialize_todo(todo))
    return response 

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    put_data = request.get_json()
    if put_data.get("completed") != None:
        todo.completed = put_data.get("completed")
    if put_data.get("text") != None:
        todo.complete = put_data.get("text")
    database.db.session.commit()
    response = jsonify({'success' : True}, Todo.serialize_todo(todo))
    return response

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    database.db.session.delete(todo)
    database.db.session.commit()
    response = jsonify({'success' : True}, Todo.serialize_todo(todo))
    return response

    
if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 80))

