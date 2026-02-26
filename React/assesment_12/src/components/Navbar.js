import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

export default function Navbar() {
  const { cart } = useCart();

  return (
    <nav className="nav">
      <Link to="/">Ecommerce</Link>
      <Link to="/cart">Cart ({cart.length})</Link>
    </nav>
  );
}