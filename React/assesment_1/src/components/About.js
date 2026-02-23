import React from "react";
import "../styles/about.css";
import aboutImg from "../assets/about.jpg";

const About = () => {
  return (
    <section className="about-section" id="about">

      <div className="section-title">
        <h2>About Me</h2>
        <div className="underline"></div>
      </div>

      <div className="about-container">

        {/* LEFT IMAGE */}
        <div className="about-left">
          <img src={aboutImg} alt="about" />
        </div>

        {/* RIGHT CONTENT */}
        <div className="about-right">

          <h3>
            A CSE student with a passion for building innovative solutions
          </h3>

          <p>
            I'm currently pursuing my Bachelor's degree in Computer Science Engineering at
            Sitarambhai Naranji Patel Institute of Technology, GTU University, expected to
            graduate in 2026. My journey in technology began with a curiosity about how things work,
            which evolved into a passion for creating meaningful digital experiences.
          </p>

          <p>
            During my academic journey, I've gained experience in various programming languages and
            technologies. I've collaborated on team projects, participated in hackathons, and
            contributed to open-source initiatives.
          </p>

          <h4 className="edu-heading">Education</h4>

          <div className="edu-box">
            <h5>Bachelor of Engineering in Computer Science</h5>
            <span>SNPIT, GTU University | 2022 - 2026</span>
            <p>CGPA: 8.5/10</p>
          </div>

          <div className="edu-box">
            <h5>Secondary and Higher Secondary Education</h5>
            <span>MG School, Pratapnagar | 2018 - 2022</span>
            <p>Avg. Percentage: 84%</p>
          </div>

          <div className="edu-box">
            <h5>Primary Education</h5>
            <span>Global International School, Rankuva | 2009 - 2018</span>
            <p>Avg. Percentage: 94%</p>
          </div>

        </div>

      </div>
    </section>
  );
};

export default About;