import React, { useState } from "react";
import "../styles/counter.css";

const Counter = () => {

  const [count, setCount] = useState(0);
  const limit = 10;

  return (
    <div className="counter-wrapper">

      <div className="counter-card">

        <h2>Smart Counter App</h2>

        <div className="count-display">
          {count}
        </div>

        {count > limit && (
          <p className="warning">
            ⚠ Limit exceeded! Try resetting.
          </p>
        )}

        <div className="btn-group">

          <button 
            className="btn decrease"
            onClick={() => setCount(count - 1)}
            disabled={count === 0}
          >
            Decrease
          </button>

          <button 
            className="btn increase"
            onClick={() => setCount(count + 1)}
          >
            Increase
          </button>

          <button 
            className="btn reset"
            onClick={() => setCount(0)}
          >
            Reset
          </button>

        </div>

      </div>

    </div>
  );
};

export default Counter;