import React from "react";

const BlogCard = ({ blog, onSelect }) => {
  return (
    <div className="blog-card" onClick={() => onSelect(blog)}>
      <h3>{blog.title}</h3>
      <p className="desc">{blog.description}</p>
      <span className="meta">{blog.author} • {blog.date}</span>
    </div>
  );
};

export default BlogCard;