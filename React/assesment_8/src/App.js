import React, { useState } from "react";
import BlogList from "./components/BlogList";
import BlogDetail from "./components/BlogDetail";
import blogData from "./blogData";
import "./styles/blog.css";

function App() {
  const [selectedBlog, setSelectedBlog] = useState(null);

  return (
    <div className="app">
      <h1>NB's Blogs</h1>

      {!selectedBlog ? (
        <BlogList blogs={blogData} onSelect={setSelectedBlog} />
      ) : (
        <BlogDetail blog={selectedBlog} onBack={() => setSelectedBlog(null)} />
      )}
    </div>
  );
}

export default App;