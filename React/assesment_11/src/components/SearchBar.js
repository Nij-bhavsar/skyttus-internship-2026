import { useRef, useEffect } from "react";

function SearchBar({ search, setSearch }) {

  const searchRef = useRef();

  useEffect(() => {
    searchRef.current.focus();
  }, []);

  return (
    <div className="search-wrapper">
      <input
        ref={searchRef}
        className="search-input"
        placeholder="🔍 Search products..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
    </div>
  );
}

export default SearchBar;