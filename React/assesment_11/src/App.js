import { useEffect, useState } from "react";
import ProductList from "./components/ProductList";
import SearchBar from "./components/SearchBar";
import FilterBar from "./components/FilterBar";
import Cart from "./components/Cart";
import { fetchProducts } from "./services/api";
import "./App.css";

function App() {

  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [cart, setCart] = useState([]);

  // API Fetch
  useEffect(() => {
    fetchProducts().then(data => {
      setProducts(data);
      setFilteredProducts(data);
    });
  }, []);

  // FILTER LOGIC
  useEffect(() => {

    let updated = products;

    // Search filter
    if (search) {
      updated = updated.filter(p =>
        p.title.toLowerCase().includes(search.toLowerCase())
      );
    }

    // Category filter
    if (category !== "All") {
      updated = updated.filter(p => p.category === category);
    }

    setFilteredProducts(updated);

  }, [search, category, products]);

  // TOGGLE CART FUNCTION
  const toggleCart = (product) => {
  setCart(prevCart => {

    const exists = prevCart.find(item => item.id === product.id);

    if (exists) {
      return prevCart.filter(item => item.id !== product.id);
    } else {
      return [...prevCart, product];
    }

  });
};

  return (
    <div className="container">

      <h1 className="nbd">BhavsarZone | Ecommerce</h1>

      <SearchBar 
        search={search}
        setSearch={setSearch}
      />

      <FilterBar 
        products={products}
        category={category}
        setCategory={setCategory}
      />

      <Cart cart={cart} />

      <ProductList 
        products={filteredProducts}
        toggleCart={toggleCart}
        cart={cart}
      />

    </div>
  );
}

export default App;