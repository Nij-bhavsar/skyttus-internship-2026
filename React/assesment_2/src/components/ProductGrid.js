import React from "react";
import ProductCard from "./ProductCard";
import products from "../data/products";

function ProductGrid({ addToCart }) {
  return (
    <div className="grid">
      {products.map((item) => (
        <ProductCard key={item.id} product={item} addToCart={addToCart} />
      ))}
    </div>
  );
}

export default ProductGrid;