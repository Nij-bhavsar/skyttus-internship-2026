import { useCart } from "../context/CartContext";

export default function Cart() {
  const { cart, removeFromCart } = useCart();

  if (cart.length === 0) {
    return <h2 style={{ padding: "20px" }}>Cart is empty</h2>;
  }

  return (
    <div>
      <h2 style={{ padding: "20px" }}>Your Cart</h2>

      {cart.map((item) => (
        <div key={item.id} className="cart-item">

          {/* Image */}
          <img src={item.image} alt={item.title} />

          {/* Product Info */}
          <div className="cart-info">
            <h4>{item.title}</h4>
            <p>₹ {item.price}</p>
          </div>

          {/* Remove Button */}
          <button onClick={() => removeFromCart(item.id)}>
            Remove
          </button>

        </div>
      ))}
    </div>
  );
}