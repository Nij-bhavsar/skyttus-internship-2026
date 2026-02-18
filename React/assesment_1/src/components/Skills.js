import React from "react";
import "../styles/skills.css";

const Skills = () => {
  return (
    <section className="skills-section" id="skills">
      
      <div className="section-title">
        <h2>My Skills</h2>
        <div className="underline"></div>
      </div>

      <h3 className="skills-subtitle">Programming Languages</h3>

      <div className="skills-grid">

        <div className="skill-card">
          <i className="fab fa-react"></i>
          <h4>React JS</h4>
        </div>

        <div className="skill-card">
          <i className="fab fa-html5"></i>
          <h4>HTML</h4>
        </div>

        <div className="skill-card">
          <i className="fab fa-css3-alt"></i>
          <h4>CSS</h4>
        </div>

        <div className="skill-card">
          <i className="fab fa-js"></i>
          <h4>JavaScript</h4>
        </div>

        <div className="skill-card">
          <i className="fab fa-python"></i>
          <h4>Python</h4>
        </div>

        <div className="skill-card">
          <i className="fab fa-java"></i>
          <h4>Java</h4>
        </div>

        <div className="skill-card">
          <i className="fas fa-database"></i>
          <h4>SQL</h4>
        </div>

      </div>
    </section>
  );
};

export default Skills;
