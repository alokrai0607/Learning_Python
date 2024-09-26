const userForm = document.getElementById("userForm");
const userList = document.getElementById("userList");
const submitButton = document.querySelector('button[type="submit"]');
const API_URL = "http://localhost:8000/users/";
let editIndex = -1;
let users = [];

window.onload = async () => {
  await fetchUsers();
};

userForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const userId = document.getElementById("user_id").value;
  const userName = document.getElementById("user_name").value;
  const userAge = document.getElementById("user_age").value;
  const userGender = document.getElementById("user_gender").value;

  const nameRegex = /^[A-Za-z\s]+$/;
  if (!nameRegex.test(userName)) {
    alert("Name should only contain alphabetic characters.");
    return;
  }

  if (userAge > 100) {
    alert("Age cannot be more than 100 years.");
    return;
  }

  if (editIndex === -1) {
    await createUser({
      user_name: userName,
      user_age: userAge,
      user_gender: userGender,
    });
  } else {
    await updateUser(userId, {
      user_name: userName,
      user_age: userAge,
      user_gender: userGender,
    });
    editIndex = -1;
    submitButton.textContent = "Submit";
  }

  userForm.reset();
  await fetchUsers();
});

async function fetchUsers() {
  const response = await fetch(API_URL);
  if (!response.ok) {
    console.error("Failed to fetch users", response.statusText);
    return;
  }
  users = await response.json();
  renderUsers();
}

async function createUser(user) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Failed to create user:", errorText);
  }
}

async function updateUser(userId, user) {
  const response = await fetch(`${API_URL}${userId}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Failed to update user:", errorText);
  }
}

async function deleteUser(userId) {
  await fetch(`${API_URL}${userId}/`, {
    method: "DELETE",
  });
  await fetchUsers();
}

function renderUsers() {
  userList.innerHTML = "";
  users.forEach((user) => {
    const userItem = document.createElement("div");
    userItem.classList.add("user-item");
    userItem.innerHTML = `<span> 
      id: ${user.user_id}, 
      Name: ${user.user_name}, 
      Age: ${user.user_age}, 
      Gender: ${user.user_gender}
      </span>      
      <div>
      <button onclick="editUser(${user.user_id})">Edit</button>
      <button onclick="confirmDelete(${user.user_id})">Delete</button>
      </div>`;
    userList.appendChild(userItem);
  });
}

function editUser(userId) {
  const user = users.find((u) => u.user_id === userId);
  document.getElementById("user_id").value = user.user_id;
  document.getElementById("user_name").value = user.user_name;
  document.getElementById("user_age").value = user.user_age;
  document.getElementById("user_gender").value = user.user_gender;
  editIndex = userId;
  submitButton.textContent = "Update";
}

function confirmDelete(userId) {
  if (confirm("Are you sure you want to delete this user?")) {
    deleteUser(userId);
  }
}
