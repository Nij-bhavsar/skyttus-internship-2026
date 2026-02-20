import React, { useState } from "react";

function WeatherApp() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const API_KEY = "ef55a99ba64a41e04893032e200a4e6e"; 

  const fetchWeather = async () => {

    if (!city.trim()) {
      setError("City name cannot be empty");
      setWeather(null);
      return;
    }

    try {
      setLoading(true);
      setError("");
      setWeather(null);

      const response = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`
      );

      if (response.status === 404) {
        throw new Error("City not found. Please check spelling.");
      }

      if (!response.ok) {
        throw new Error("Something went wrong. Try again later.");
      }

      const data = await response.json();
      setWeather(data);

    } catch (err) {

      if (err.message.includes("fetch")) {
        setError("Network error. Check your internet connection.");
      } else {
        setError(err.message);
      }

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="weather-card">

      {/* SEARCH BAR */}
      <div className="search-box">
        <input
          type="text"
          placeholder="Enter city name..."
          value={city}
          onChange={(e) => {
            setCity(e.target.value);
            setError("");
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") fetchWeather();
          }}
        />
        <button onClick={fetchWeather}>🔍</button>
      </div>

      {/* LOADING */}
      {loading && <p className="loading">Fetching weather...</p>}

      {/* ERROR */}
      {error && <p className="error">{error}</p>}

      {/* WEATHER INFO */}
      {weather && (
        <div className="weather-info">
          <h2>{weather.name}</h2>
          <p className="temp">The Temperature is {Math.round(weather.main.temp)}°C</p>
          <p className="desc">{weather.weather[0].description}</p>
          <p>Humidity: {weather.main.humidity}%</p>
          <p>Wind: {weather.wind.speed} mph</p>
        </div>
      )}

    </div>
  );
}

export default WeatherApp;