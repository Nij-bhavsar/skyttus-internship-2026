import ProductCard from "./ProductCard";
import useFetchProducts from "../hooks/useFetchProducts";

function ProductList() {
  const { products, loading, error } = useFetchProducts();

  if (loading) return <h2 className="status">Loading Products...</h2>;
  if (error) return <h2 className="status error">{error}</h2>;

  return (
    <div className="product-grid">
      {products.map(product => (
        <ProductCard key={product.id} product={product}/>
      ))}
    </div>
  );
}

export default ProductList;