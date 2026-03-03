import { useDashboard } from "../../context/DashboardContext";

const Users = () => {
  const { data, loading } = useDashboard();

  if (loading) return <p className="status">Loading...</p>;

  return (
    <div className="page">
      <h2>👥 Users</h2>
      <ul className="user-list">
        {data.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Users;