const apiBaseUrl = "http://localhost:8000/todos";

// Get references to the DOM elements
const todoTitleInput = document.getElementById("todo-title");
const todoDescriptionInput = document.getElementById("todo-description");
const addTodoButton = document.getElementById("add-todo-btn");
const todoList = document.getElementById("todo-list");

// Add Todo Function
addTodoButton.addEventListener("click", async () => {
  const title = todoTitleInput.value;
  const description = todoDescriptionInput.value;

  if (title && description) {
    const newTodo = {
      title: title,
      description: description,
    };

    await fetch(apiBaseUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newTodo),
    });

    todoTitleInput.value = "";
    todoDescriptionInput.value = "";

    fetchTodos();
  } else {
    alert("Please enter both title and description.");
  }
});

// Fetch Todos Function
async function fetchTodos() {
  const response = await fetch(apiBaseUrl);
  const todos = await response.json();

  renderTodos(todos);
}

// Render Todos Function
function renderTodos(todos) {
  todoList.innerHTML = "";

  todos.forEach((todo) => {
    const li = document.createElement("li");
    li.className = "todo-item";

    li.innerHTML = `
            <div>
                <span class="todo-title">${todo.title}</span>
                <p class="todo-description">${todo.description}</p>
            </div>
            <div class="todo-actions">
                <button onclick="deleteTodo(${todo.id})">Delete</button>
            </div>
        `;

    todoList.appendChild(li);
  });
}

// Delete Todo Function
async function deleteTodo(id) {
  await fetch(`${apiBaseUrl}/${id}`, {
    method: "DELETE",
  });

  fetchTodos();
}

// Initial Fetch
fetchTodos();
