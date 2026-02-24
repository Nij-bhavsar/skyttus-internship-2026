import React from "react";

const UserCard = ({ user, toggleStatus, removeUser }) => {

  return (
    <div className={`user-card ${user.active ? "active" : ""}`}>

      <h3>{user.name}</h3>
      <p>{user.email}</p>

      <span className={`status ${user.active ? "on" : "off"}`}>
        {user.active ? "Active" : "Inactive"}
      </span>

      <div className="btn-group">

        <button 
          className="btn toggle"
          onClick={() => toggleStatus(user.id)}
        >
          Toggle Status
        </button>

        <button 
          className="btn delete"
          onClick={() => removeUser(user.id)}
        >
          Remove
        </button>

      </div>

    </div>
  );
};

export default UserCard;