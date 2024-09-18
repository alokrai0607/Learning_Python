// Define the base URL for the API endpoints
const apiBaseUrl = "http://localhost:8000/todos";

// Get references to HTML elements (title input, description input, add button, and the todo list)
const todoTitleInput = document.getElementById("todo-title");
const todoDescriptionInput = document.getElementById("todo-description");
const addTodoButton = document.getElementById("add-todo-btn");
const todoList = document.getElementById("todo-list");

// Variables to track if we're in edit mode and which todo is being edited
let isEditMode = false;
let editTodoId = null;

// Event listener for adding or updating todos
addTodoButton.addEventListener("click", async () => {
  // Fetch the title and description from input fields
  const title = todoTitleInput.value;
  const description = todoDescriptionInput.value;

  // Validate that both title and description are present
  if (title && description) {
    const todoData = {
      title: title,
      description: description,
    };

    // Check if we're in edit mode
    if (isEditMode) {
      // Update the todo if edit mode is active
      await updateTodo(editTodoId, todoData);
      isEditMode = false; // Reset edit mode
      editTodoId = null; // Clear the ID of the todo being edited
      addTodoButton.textContent = "Add Todo"; // Change button text back to 'Add'
    } else {
      // Otherwise, create a new todo
      await createTodo(todoData);
    }
    // Clear the input fields after adding/updating
    todoTitleInput.value = "";
    todoDescriptionInput.value = "";
    // Fetch and display the updated todo list
    fetchTodos();
  } else {
    // Alert if inputs are missing
    alert("Please enter both title and description.");
  }
});

// Function to create a new todo (POST request)
async function createTodo(todoData) {
  await fetch(apiBaseUrl, {
    method: "POST", // Create a new todo
    headers: {
      "Content-Type": "application/json", // Tell the server we're sending JSON
    },
    body: JSON.stringify(todoData), // Convert the todo data to a JSON string
  });
}

// Function to update an existing todo (PUT request)
async function updateTodo(todoId, todoData) {
  await fetch(`${apiBaseUrl}/${todoId}`, {
    method: "PUT", // Update an existing todo
    headers: {
      "Content-Type": "application/json", // Tell the server we're sending JSON
    },
    body: JSON.stringify(todoData), // Convert the updated todo data to JSON string
  });
}

// Fetch all todos from the server (GET request)
async function fetchTodos() {
  const response = await fetch(apiBaseUrl); // Make a GET request to fetch all todos
  const todos = await response.json(); // Convert the response to JSON
  renderTodos(todos); // Pass the todos to the render function to display them
}

// Render the todo list in the HTML (Display todos)
function renderTodos(todos) {
  todoList.innerHTML = ""; // Clear the current list before rendering

  // Loop through the todos array and create HTML for each todo
  todos.forEach((todo) => {
    const li = document.createElement("li"); // Create a list item (li)
    li.className = "todo-item"; // Add a class for styling

    // Add HTML structure inside the li with todo title, description, and action buttons
    li.innerHTML = `
      <div>
        <span class="todo-title">${todo.title}</span>
        <p class="todo-description">${todo.description}</p>
      </div>
      <div class="todo-actions">
        <button onclick="editTodo(${todo.id}, '${todo.title}', '${todo.description}')">Edit</button>
        <button onclick="deleteTodo(${todo.id})">Delete</button>
      </div>
    `;
    todoList.appendChild(li); // Append each todo to the list
  });
}

// Edit an existing todo
function editTodo(id, title, description) {
  // Fill the input fields with the todo's current values
  todoTitleInput.value = title;
  todoDescriptionInput.value = description;

  // Enable edit mode and store the todo's ID
  isEditMode = true;
  editTodoId = id;

  // Change the button text to indicate we're in update mode
  addTodoButton.textContent = "Update Todo";
}

// Delete a todo (DELETE request)
async function deleteTodo(id) {
  await fetch(`${apiBaseUrl}/${id}`, {
    method: "DELETE", // Send a DELETE request to remove the todo
  });
  fetchTodos(); // Refresh the todo list after deletion
}

// Initial fetch to load the todos when the page loads
fetchTodos();
