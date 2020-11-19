import React from 'react';

const Todo = ({ text, todo, todos, setTodos }) => {
    //Events
    const deleteHandler = () => {
        //setTodos(todos.filter(el => el.id !== todo.id));
        const deleteData = {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        };
        fetch("/todos/" + todo.id, deleteData)
            .then(response => response.json())
            .then(data => {
                setTodos(todos.filter(td => td !== todo));
            })
        .catch(error => console.log(error))
    };
    const completeHandler = () => {
        /*
        setTodos(todos.map(item => {
            if(item.id === todo.id){
                return {
                    ...item, completed: !item.completed
                };
            }
            return item;
        })
        
      );
      */
        
        const index = todos.indexOf(todo);
        const putData = {
            method: "PUT",
            body: JSON.stringify({ completed: !todo.completed}),
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        };
        fetch("/todos/" + todo.id, putData)
            .then(response => response.json())
            .then(({ todo }) => {
                todos[index] = { id: todo.id, name: todo.name, completed: todo.completed};
                setTodos(todos)
            })
            .catch(error => console.log(error));
    };

    return(
        <div className="todo">
            <li className={`todo-item ${todo.completed ? "completed" : ""}`}>{text}</li>
            <button onClick={completeHandler} className="complete-btn">
                <i className="fas fa-check"></i>
            </button>
            <button onClick={deleteHandler} className="trash-btn">
                <i className="fas fa-trash"></i>
            </button>
        </div>
    );
};



export default Todo