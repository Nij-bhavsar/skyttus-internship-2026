function ProductCard({ product }) {
  return (
    <div className="product-card">

      <span className="price">₹ {product.price}</span>

      <img src={product.thumbnail} alt={product.title} />

      <h3>{product.title}</h3>

      <p className="brand">{product.brand}</p>

      <div className="rating">
        ⭐ {product.rating}
      </div>

      <button>View Product</button>

    </div>
  );
}

export default ProductCard;