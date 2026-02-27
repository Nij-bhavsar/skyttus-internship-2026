import { useAuth } from "../context/AuthContext";
import "./Profile.css";

const Profile = () => {
  const { user } = useAuth();

  return (
    <div className="profile-container">
      <h1>My Profile</h1>

      <div className="profile-card">
        <p>
          <strong>Username:</strong> {user?.username}
        </p>

        <p>
          <strong>Role:</strong> User
        </p>

        <p>
          <strong>Status:</strong> Active
        </p>
      </div>
    </div>
  );
};

export default Profile;