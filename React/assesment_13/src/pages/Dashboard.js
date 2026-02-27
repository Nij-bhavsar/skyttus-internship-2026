import { useAuth } from "../context/AuthContext";
import "./Dashboard.css";

const Dashboard = () => {
  const { user } = useAuth();

  return (
    <div className="dashboard">
      <h1>Welcome, {user?.username} 🎉</h1>
      <p>You are successfully logged in.</p>

      <div className="cards">
        <div className="card">
          <h3>Profile</h3>
          <p>View your account details</p>
        </div>

        <div className="card">
          <h3>Settings</h3>
          <p>Manage your preferences</p>
        </div>

        <div className="card">
          <h3>Security</h3>
          <p>Update password & access</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;