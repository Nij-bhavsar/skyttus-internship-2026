import React from "react";
import SearchBar from "./SearchBar";

function Header({ cartCount }) {
  return (
    <header className="header">
      <div className="logo">BhavsarZone</div>

      <nav>
        <a href="#">Home</a>
        <a href="#">Products</a>
        <a href="#">Deals</a>
        <a href="#">Contact</a>
      </nav>

      <SearchBar />

      <div className="cart">
        🛒 Cart <span>{cartCount}</span>
      </div>
    </header>
  );
}

export default Header;