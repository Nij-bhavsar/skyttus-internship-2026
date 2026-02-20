const form = document.getElementById("todoForm");
const input = document.getElementById("todoInput");
const list = document.getElementById("todoList");
const errorMsg = document.getElementById("errorMsg");

let todos = JSON.parse(localStorage.getItem("todos")) || [];

// Render Todos
function renderTodos() {
  list.innerHTML = "";
  todos.forEach((todo, index) => {
    const li = document.createElement("li");
    li.className = todo.completed ? "completed" : "";

    li.innerHTML = `
      <span>${todo.text}</span>
      <div class="actions">
        <button class="edit" data-index="${index}">Edit</button>
        <button class="delete" data-index="${index}">Delete</button>
        <input type="checkbox" class="toggle" data-index="${index}" ${todo.completed ? "checked" : ""}/>
      </div>
    `;

    list.appendChild(li);
  });

  localStorage.setItem("todos", JSON.stringify(todos));
}

// Add Todo
form.addEventListener("submit", function(e) {
  e.preventDefault();

  if (input.value.trim() === "") {
    errorMsg.textContent = "Task cannot be empty!";
    return;
  }

  errorMsg.textContent = "";

  todos.push({
    text: input.value,
    completed: false
  });

  input.value = "";
  renderTodos();
});

// Event Delegation
list.addEventListener("click", function(e) {
  const index = e.target.dataset.index;

  if (e.target.classList.contains("delete")) {
    todos.splice(index, 1);
    renderTodos();
  }

  if (e.target.classList.contains("edit")) {
    const newText = prompt("Edit your task:");
    if (newText) {
      todos[index].text = newText;
      renderTodos();
    }
  }
});

// Toggle Complete
list.addEventListener("change", function(e) {
  if (e.target.classList.contains("toggle")) {
    const index = e.target.dataset.index;
    todos[index].completed = e.target.checked;
    renderTodos();
  }
});

// Initial Load
renderTodos();