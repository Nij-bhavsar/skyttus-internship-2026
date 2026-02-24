import React from "react";
import Button from "../UI/Button";

function UserItem({ user, deleteUser, setEditUser }) {
  return (
    <div className="user-item">
      <div>
        <h3>{user.name}</h3>
        <p>{user.email}</p>
        <small>{user.note}</small>
      </div>

      <div>
        <Button className="edit-btn" onClick={() => setEditUser(user)}>Edit</Button>
        <Button className="delete-btn" onClick={() => deleteUser(user.id)}>Delete</Button>
      </div>
    </div>
  );
}

export default UserItem;