import React, { useState } from "react";
import "../styles/projects.css";

// ✅ Import images from assets folder
import goguide from "../assets/goguide.png";
import resumeBuilder from "../assets/resume_web.png";
import tracelly from "../assets/tracelly.png";
import gamingHub from "../assets/nb_game.png";
import portfolio from "../assets/portfolio.png";

const Projects = () => {

  const [filter, setFilter] = useState("All");

  // ✅ Use imported image variables instead of string paths
  const projectData = [
    {
      title: "Go Guide",
      category: "Web",
      image: goguide,
      desc: "A travelling guide app for tourists.",
      tags: ["HTML", "CSS", "JavaScript"]
    },
    {
      title: "Resume Builder Web",
      category: "Web",
      image: resumeBuilder,
      desc: "A website that creates simple resumes.",
      tags: ["React JS"]
    },
    {
      title: "Tracelly - Lost & Found",
      category: "Web",
      image: tracelly,
      desc: "Website to report lost items easily.",
      tags: ["React JS", "Node", "Express"]
    },
    {
      title: "NB's Gaming Hub",
      category: "Mobile",
      image: gamingHub,
      desc: "Website with simple games.",
      tags: ["React JS"]
    },
    {
      title: "My Portfolio",
      category: "Web",
      image: portfolio,
      desc: "My personal portfolio website.",
      tags: ["HTML", "CSS", "JavaScript"]
    }
  ];

  const filteredProjects = filter === "All"
    ? projectData
    : projectData.filter(p => p.category === filter);

  return (
    <section className="projects-section" id="projects">

      <div className="section-title">
        <h2>Projects</h2>
        <div className="underline"></div>
      </div>

      <div className="project-filters">
        <button onClick={() => setFilter("All")}>All</button>
        <button onClick={() => setFilter("Web")}>Web</button>
        <button onClick={() => setFilter("Mobile")}>Mobile</button>
        <button onClick={() => setFilter("ML")}>ML/AI</button>
      </div>

      <div className="projects-grid">
        {filteredProjects.map((p, index) => (
          <div className="project-card" key={index}>

            <img src={p.image} alt={p.title} />

            <div className="project-content">
              <h4>{p.title}</h4>
              <p>{p.desc}</p>

              <div className="project-tags">
                {p.tags.map((tag, i) => (
                  <span key={i}>{tag}</span>
                ))}
              </div>
            </div>

          </div>
        ))}
      </div>

    </section>
  );
};

export default Projects;
