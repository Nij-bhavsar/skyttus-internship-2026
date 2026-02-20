import React from "react";
import WeatherApp from "./components/WeatherApp";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🌤 Weather Dashboard</h1>
        <p>Check the Real-Time Weather of Any City</p>
      </header>

      <main>
        <WeatherApp />
      </main>

      <footer className="app-footer">
        <p>© 2026 Weather App | Nij Bhavsar</p>
      </footer>
    </div>
  );
}

export default App;