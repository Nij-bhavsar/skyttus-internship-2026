import bg from "../assets/bg1.jpg";
const Home = () => {
  return (
    <section id="home" className="hero-section">
      <div className="container">
        <div className="hero-content">

          <div className="hero-text">
            <p className="intro">Hi, my name is</p>
            <h1 className="name">Nij D. Bhavsar</h1>
            <h2 className="tagline">I build things for the web.</h2>

            <p className="description">
              I'm a fourth-year Computer Science Engineering student specializing in full-stack development.
              I'm passionate about creating intuitive and efficient digital experiences.
            </p>

            <div className="cta-buttons">
              <a href="#projects" className="primary-btn">View Projects</a>
              <a href="#contact" className="secondary-btn">Contact Me</a>
            </div>
          </div>

          <div className="hero-image">
            <div className="image-container">
              <img src={bg} alt="nij" />
            </div>
          </div>

        </div>
      </div>
    </section>
  );
};

export default Home;
