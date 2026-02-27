import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import "../styles/auth.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const { login } = useAuth();
  const navigate = useNavigate();

  // ✅ MOCK LOGIN HANDLER
  const handleSubmit = (e) => {
    e.preventDefault();
    setError("");

    // mock credentials
    if (username === "Nij" && password === "nij@123") {
      login({ username: "Nij Bhavsar" });
      navigate("/dashboard");
    } else {
      setError("Invalid username or password");
    }
  };

  return (
    <div className="auth-container">
      <form className="auth-card" onSubmit={handleSubmit}>
        <h2>Welcome Back 👋</h2>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Login</button>

        <p style={{ fontSize: "12px", marginTop: "10px", color: "#555" }}>
          <b>Demo Credentials</b><br />
          Username: <b>Nij</b><br />
          Password: <b>nij@123</b>
        </p>
      </form>
    </div>
  );
};

export default Login;