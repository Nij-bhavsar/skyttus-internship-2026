function ProductCard({ product, toggleCart, cart }) {

  const inCart = cart.some(item => item.id === product.id);

  return (
    <div className="product-card">

      <span className="price">₹ {product.price}</span>

      <img src={product.thumbnail} alt={product.title} />

      <h3>{product.title}</h3>

      <p className="brand">{product.brand}</p>

      <div className="rating">
        ⭐ {product.rating}
      </div>

      <button
        type="button"
        className={inCart ? "added-btn" : ""}
        onClick={() => toggleCart(product)}
      >
        {inCart ? "✔ Added" : "Add to Cart"}
      </button>

    </div>
  );
}

export default ProductCard;