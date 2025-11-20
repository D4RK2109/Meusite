
const users = [
  { id: 1, name: "Leanne Graham", username: "Bret", email: "Sincere@april.biz" },
  { id: 2, name: "Ervin Howell", username: "Antonette", email: "Shanna@melissa.tv" }
];

const userList = document.getElementById("user-list");
users.forEach(user => {
  const li = document.createElement("li");
  li.textContent = `${user.name} (${user.username}) - ${user.email}`;
  userList.appendChild(li);
});
