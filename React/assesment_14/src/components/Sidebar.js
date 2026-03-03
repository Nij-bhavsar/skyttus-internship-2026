import { NavLink } from "react-router-dom";

const Sidebar = ({ isOpen }) => {
  return (
    <div className={`sidebar ${isOpen ? "open" : "closed"}`}>
      <h2 className="logo">Assessment 14</h2>

      <NavLink to="/dashboard/overview">Overview</NavLink>
      <NavLink to="/dashboard/products">Products</NavLink>
      <NavLink to="/dashboard/users">Users</NavLink>
    </div>
  );
};

export default Sidebar;