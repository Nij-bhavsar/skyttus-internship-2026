function Cart({ cart }) {
  return (
    <div className="cart-box">
      🛒 Cart Items: {cart.length}
    </div>
  );
}

export default Cart;