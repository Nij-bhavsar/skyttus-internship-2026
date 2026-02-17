import React, { useEffect, useRef } from "react";
import "../styles/contact.css";
import { FaEnvelope, FaPhoneAlt, FaMapMarkerAlt, FaGithub, FaLinkedinIn, FaInstagram, FaFacebookF } from "react-icons/fa";
import { useLocation } from "react-router-dom";

const Contact = () => {
  const location = useLocation();
  const nameRef = useRef(null);
  const emailRef = useRef(null);
  const subjectRef = useRef(null);

  useEffect(() => {
    // If navigation included project info, focus the name input and prefill subject
    if (location.state && location.state.fromProject) {
      if (nameRef.current) nameRef.current.focus();
      if (subjectRef.current) subjectRef.current.value = `Regarding: ${location.state.fromProject}`;
    }
  }, [location.state]);

  return (
    <section className="contact-section" id="contact">

      <div className="section-title">
        <h2>Contact Me</h2>
        <div className="underline"></div>
      </div>

      <div className="contact-container">

        {/* LEFT SIDE */}
        <div className="contact-left">

          <h3>Get In Touch</h3>

          <p>
            Feel free to reach out to me for any opportunities,
            collaborations, or just to say hello!
          </p>

          <div className="contact-item">
            <FaEnvelope className="icon" />
            <span>nijbhavsar4433@gmail.com</span>
          </div>

          <div className="contact-item">
            <FaPhoneAlt className="icon" />
            <span>+91 9313234412</span>
          </div>

          <div className="contact-item">
            <FaMapMarkerAlt className="icon" />
            <span>Navsari, Gujarat, India</span>
          </div>

          <div className="social-icons">
            <a href="https://github.com/dashboard"><FaGithub /></a>
            <a href="http://www.linkedin.com/in/nij-bhavsar-cse"><FaLinkedinIn /></a>
            <a href="https://www.instagram.com/the_nb.23?igsh=MWE4ZnpoY3M1bGUyeA=="><FaInstagram /></a>
            <a href="https://www.facebook.com/share/1EN29v6Yu9/"><FaFacebookF /></a>
          </div>

        </div>

        {/* RIGHT SIDE */}
        <div className="contact-right">

          <form>

            <input ref={nameRef} type="text" placeholder="Your Name" required />
            <input ref={emailRef} type="email" placeholder="Your Email" required />
            <input ref={subjectRef} type="text" placeholder="Subject" />
            <textarea placeholder="Your Message"></textarea>

            <button type="submit">Send Message</button>

          </form>

        </div>

      </div>
    </section>
  );
};

export default Contact;
