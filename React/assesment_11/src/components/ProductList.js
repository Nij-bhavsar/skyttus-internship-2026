import ProductCard from "./ProductCard";

function ProductList({ products, toggleCart, cart }) {
  return (
    <div className="product-grid">
      {products.map(product => (
        <ProductCard
          key={product.id}
          product={product}
          toggleCart={toggleCart}
          cart={cart}
        />
      ))}
    </div>
  );
}

export default ProductList;