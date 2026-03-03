const Header = ({ toggleSidebar }) => {
  return (
    <div className="header">
      <button className="menu-btn" onClick={toggleSidebar}>
        ☰
      </button>

      <h3>Dashboard</h3>
      <span className="admin">👤 Admin</span>
    </div>
  );
};

export default Header;