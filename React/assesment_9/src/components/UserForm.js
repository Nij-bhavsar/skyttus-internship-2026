import React, { useState, useEffect, useRef } from "react";
import Input from "../UI/Input";
import Button from "../UI/Button";

function UserForm({ addUser, editUser, updateUser }) {

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const noteRef = useRef(); // Uncontrolled input

  useEffect(() => {
    if(editUser){
      setName(editUser.name);
      setEmail(editUser.email);
      noteRef.current.value = editUser.note;
    }
  }, [editUser]);

  const submitHandler = (e) => {
    e.preventDefault();

    const userData = {
      id: editUser ? editUser.id : Date.now(),
      name,
      email,
      note: noteRef.current.value
    };

    if(editUser){
      updateUser(userData);
    } else {
      addUser(userData);
    }

    setName("");
    setEmail("");
    noteRef.current.value = "";
  };

  return (
    <div className="card">
      <form onSubmit={submitHandler}>
        <Input value={name} onChange={e => setName(e.target.value)} placeholder="Enter Name" />
        <Input value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter Email" />

        {/* Uncontrolled */}
        <input ref={noteRef} placeholder="Enter Note (Uncontrolled)" />

        <Button className="add-btn" type="submit">
          {editUser ? "Update User" : "Add User"}
        </Button>
      </form>
    </div>
  );
}

export default UserForm;