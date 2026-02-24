import React from "react";
import BlogCard from "./BlogCard";

const BlogList = ({ blogs, onSelect }) => {
  return (
    <div className="blog-grid">
      {blogs.map(blog => (
        <BlogCard key={blog.id} blog={blog} onSelect={onSelect} />
      ))}
    </div>
  );
};

export default BlogList;