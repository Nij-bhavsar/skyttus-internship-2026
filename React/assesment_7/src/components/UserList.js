import React, { useState } from "react";
import UserCard from "./UserCard";
import "../styles/users.css";

const UserList = () => {

  const [users, setUsers] = useState([
    { id: 1, name: "Nij Bhavsar", email: "nij@gmail.com", active: true },
    { id: 2, name: "Sanjay Patel", email: "sanjay@gmail.com", active: false },
    { id: 3, name: "Drish Bhandari", email: "drish@gmail.com", active: true },
    { id: 4, name: "Meet Patel", email: "meet@gmail.com", active: false },
    { id: 5, name: "Het Patel", email: "het@gmail.com", active: true },
    { id: 6, name: "Henil Patel", email: "henil@gmail.com", active: true },
    { id: 7, name: "Dhruv Patel", email: "dhruv@gmail.com", active: false },
    { id: 8, name: "Jeet Bhavsar", email: "jeet@gmail.com", active: false }

  ]);

  const toggleStatus = (id) => {
    const updatedUsers = users.map(user =>
      user.id === id ? { ...user, active: !user.active } : user
    );
    setUsers(updatedUsers);
  };

  const removeUser = (id) => {
    setUsers(users.filter(user => user.id !== id));
  };

  return (
    <div className="user-wrapper">

      <h2>User Management System</h2>

      {users.length === 0 ? (
        <p className="no-users">No users available</p>
      ) : (
        <div className="user-grid">
          {users.map(user => (
            <UserCard 
              key={user.id}
              user={user}
              toggleStatus={toggleStatus}
              removeUser={removeUser}
            />
          ))}
        </div>
      )}

    </div>
  );
};

export default UserList;