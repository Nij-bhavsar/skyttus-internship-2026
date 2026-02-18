import React, { useState } from "react";
import { Link, useLocation } from "react-router-dom";

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const location = useLocation();

  const closeMenu = () => setMenuOpen(false);

  const isActive = (path) => location.pathname === path ? "active" : "";

  return (
    <header className="header" id="header">
      <div className="container">

        <div className="logo">
          <h1>
            <Link to="/"><span>NIJ BHAVSAR | PORTFOLIO</span></Link>
          </h1>
        </div>

        <div className="hamburger" onClick={() => setMenuOpen(!menuOpen)}>
          <div className="line"></div>
          <div className="line"></div>
          <div className="line"></div>
        </div>

        <nav className={`navbar ${menuOpen ? "active" : ""}`}>
          <ul>
            <li><Link to="/" className={`nav-link ${isActive("/")}`} onClick={closeMenu}>Home</Link></li>
            <li><Link to="/about" className={`nav-link ${isActive("/about")}`} onClick={closeMenu}>About</Link></li>
            <li><Link to="/skills" className={`nav-link ${isActive("/skills")}`} onClick={closeMenu}>Skills</Link></li>
            <li><Link to="/projects" className={`nav-link ${isActive("/projects")}`} onClick={closeMenu}>Projects</Link></li>
            <li><Link to="/contact" className={`nav-link ${isActive("/contact")}`} onClick={closeMenu}>Contact</Link></li>
          </ul>
        </nav>

      </div>
    </header>
  );
};

export default Header;
