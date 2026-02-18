import bg from "../assets/bg1.jpg";
import resume from "../assets/Nij_Bhavsar_Resume.pdf"
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

            <nav className={`navbar "active" : ""}`}>
            <a
              href={resume}
              className="resume-btn"
              download="Nij_Bhavsar_Resume.pdf"
            >
              Download My Resume
            </a>
            </nav>
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
