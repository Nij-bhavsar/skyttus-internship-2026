import React, { useState } from "react";import Header from "./components/Header";
import Banner from "./components/Banner";
import ProductGrid from "./components/ProductGrid";
import Footer from "./components/Footer";
import "./App.css";

function App() {
    const [cart, setCart] = useState([]);

    const addToCart = (product) => {
    setCart([...cart, product]);
  };
  return (
    <div>
      <Header cartCount={cart.length} />
      <Banner />
      <ProductGrid addToCart={addToCart}/>
      <Footer />
    </div>
  );
}

export default App;