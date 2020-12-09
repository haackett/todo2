import React from 'react';

const Form = ({ inputText, setInputText, todos, setTodos, setStatus}) => {
    
    //Events
    const inputTextHandler = (e) => {
        setInputText(e.target.value);
    };
    const submitTodoHandler = (e) => {
        e.preventDefault();
        /*
        setTodos([
            ...todos, 
            {text: inputText, completed: false, id: Date.now()},
        ]);
        */
        const postData = {
            method: "POST",
            body: JSON.stringify({ text: inputText, requesting_user : 'Website' }),
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Origin" : "localhost:3000"
            }
        };
        console.log(postData)
        fetch("/todos/", postData)
            .then(response => response.json())
            .then(( todo ) => {
                todos.push({id: todo.id, text: todo.text, completed: todo.completed});
                setTodos(todos);
            })
            .catch(error => console.log(error));
        setInputText('');
    };
    const statusHandler = (e) => {
        setStatus(e.target.value);
    };
    return(
        <form>
            <input 
                value={inputText} 
                onChange={inputTextHandler} 
                type="text" 
                className="todo-input" 
            />
            <button onClick={submitTodoHandler} className="todo-button" type="submit">
                <i className= "fas fa-plus-square"></i>
            </button>
            <div className="select">
                <select onChange={statusHandler} name="todos" className="filter-todo">
                    <option value="all">All</option>
                    <option value="completed">Completed</option>
                    <option value="incompleted">Incompleted</option>
                </select>
            </div>
        </form>
    );
};

export default Form