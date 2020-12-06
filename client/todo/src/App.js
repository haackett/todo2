import React, { useState, useEffect, Component } from 'react';

//Import Components
import Form from './components/Form';
import TodoList from './components/TodoList';

function App() {
  //State
  const [inputText, setInputText] = useState("");
  const [todos, setTodos] = useState([]);
  const [status, setStatus] = useState("all");
  const [filteredTodos, setFilteredTodos] = useState([]);
   
  //USE EFFECT
  useEffect(() => {
    fetch("/todos/")
      .then(response => response.json())
      .then(data => setTodos(data))
      .catch(error => console.log(error));
      
    filterHandler();
  }, [todos, status]);

  //Functions
  const filterHandler = () => {
    
    switch(status){
      case 'completed':
        setFilteredTodos(todos.filter(todo => todo.completed === true))
        break;
      case 'incompleted':
        setFilteredTodos(todos.filter(todo => todo.completed === false))
        break;
      default:
        setFilteredTodos(todos)
        break;
    }
  }
 
  return (
    <div className="App">
      <header> todo list </header>
      <Form 
        inputText={inputText} 
        todos={todos} 
        setTodos={setTodos} 
        setInputText={setInputText}
        status={status}
        setStatus={setStatus}
      />
      <TodoList 
        todos={todos} 
        setTodos={setTodos} 
        filteredTodos={filteredTodos}
      />
    </div>
  );
};



export default App;
