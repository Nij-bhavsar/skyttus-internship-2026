import React, { useState, useEffect } from "react";
import "../components/Form.css";

const Form = () => {

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: ""
  });

  const [errors, setErrors] = useState({});
  const [strength, setStrength] = useState("");
  const [success, setSuccess] = useState("");

  useEffect(() => {
    sessionStorage.setItem("formData", JSON.stringify(formData));
  }, [formData]);

  const validate = (name, value) => {
    let error = "";

    if (!value) error = "Required";

    if (name === "email") {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(value)) error = "Invalid Email";
    }

    if (name === "password") {
      if (value.length < 6) {
        error = "Min 6 characters";
        setStrength("Weak");
      } else if (value.length < 10) {
        setStrength("Medium");
      } else {
        setStrength("Strong");
      }
    }

    setErrors(prev => ({ ...prev, [name]: error }));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    validate(name, value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSuccess("");

    Object.keys(formData).forEach(key => {
      validate(key, formData[key]);
    });

    const hasError = Object.values(errors).some(err => err !== "");

    if (!hasError && formData.name && formData.email && formData.password) {
      setSuccess("Successfully Submitted 🚀");
    }
  };

  const handleReset = () => {
    setFormData({ name: "", email: "", password: "" });
    setErrors({});
    setStrength("");
    setSuccess("");
    sessionStorage.removeItem("formData");
  };

  return (
    <div className="form-wrapper">

      <div className="glass-card">
        <h2>Create an Account</h2>

        {success && <div className="success-msg">{success}</div>}

        <form onSubmit={handleSubmit}>

          <div className="input-group">
  <label>Full Name</label>
  <input type="text" name="name"
    value={formData.name}
    onChange={handleChange}
    onBlur={handleChange}
  />
  {errors.name && <span className="error">{errors.name}</span>}
</div>

<div className="input-group">
  <label>Email Address</label>
  <input type="email" name="email"
    value={formData.email}
    onChange={handleChange}
    onBlur={handleChange}
  />
  {errors.email && <span className="error">{errors.email}</span>}
</div>

<div className="input-group">
  <label>Password</label>
  <input type="password" name="password"
    value={formData.password}
    onChange={handleChange}
    onBlur={handleChange}
  />
  {strength && <div className={`strength ${strength.toLowerCase()}`}>{strength}</div>}
  {errors.password && <span className="error">{errors.password}</span>}
</div>

          <div className="btn-group">
            <button type="submit" className="submit-btn">Submit</button>
            <button type="button" className="reset-btn" onClick={handleReset}>Reset</button>
          </div>

        </form>
      </div>
    </div>
  );
};

export default Form;