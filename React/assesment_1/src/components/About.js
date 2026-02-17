const About = () => {
  return (
    <section id="about" className="about-section">
      <div className="container">

        <div className="section-title">
          <h2>About Me</h2>
          <span className="line"></span>
        </div>

        <div className="about-content">

          <div className="about-image">
            <img
              src="https://images.pexels.com/photos/5428836/pexels-photo-5428836.jpeg"
              alt="About nij"
            />
          </div>

          <div className="about-text">
            <h3>A CSE student with a passion for building innovative solutions</h3>

            <p>
               I'm currently pursuing my Bachelor's degree in Computer Science Engineering at Sitarambhai Naranji Patel
            Institute of Technology, GTU University, expected to graduate in 2026. My journey in technology began with a
            curiosity about how things work, which evolved into a passion for creating meaningful digital experiences.
            </p>

            <div className="education">

              <h4>Education</h4>

              <div className="education-item">
                <h5>Bachelor of Engineering</h5>
                <p>S. N. Patel Institute Of Technology, Bardoli | 2022 - 2026</p>
                <p>CGPA: 8.5/10</p>
              </div>

              <div className="education-item">
                <h5>Secondary Education</h5>
                <p>MG School, Pratapnagar | 2018 - 2022</p>
                <p>Avg. Percentage: 84%</p>
              </div>
              <div className="education-item">
                <h5>Primary Education</h5>
                <p>Global International School, Rankuva | 2016 - 2018</p>
                <p>Avg. Percentage: 95%</p>
              </div>

            </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default About;
