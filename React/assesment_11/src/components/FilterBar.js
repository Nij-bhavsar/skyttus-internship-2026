function FilterBar({ products, category, setCategory }) {

  const categories = ["All", ...new Set(products.map(p => p.category))];

  return (
    <div className="filter-wrapper">
      <select 
        className="filter-select"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      >
        {categories.map(cat => (
          <option key={cat}>{cat}</option>
        ))}
      </select>
    </div>
  );
}

export default FilterBar;