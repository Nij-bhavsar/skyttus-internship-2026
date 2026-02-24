import React from "react";

const BlogDetail = ({ blog, onBack }) => {
  return (
    <div className="blog-detail">
      <button className="back-btn" onClick={onBack}>← Back</button>

      <h2>{blog.title}</h2>
      <p className="meta">{blog.author} • {blog.date}</p>
      <p className="content">{blog.content}</p>
    </div>
  );
};

export default BlogDetail;