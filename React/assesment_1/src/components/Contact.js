import React from "react";
import "../styles/contact.css";
import { FaEnvelope, FaPhoneAlt, FaMapMarkerAlt, FaGithub, FaLinkedinIn, FaInstagram, FaFacebookF } from "react-icons/fa";

const Contact = () => {
  return (
    <section className="contact-section" id="contact">

      <div className="section-title">
        <h2>Contact Me</h2>
        <div className="underline"></div>
      </div>

      <div className="contact-wrapper">

        {/* LEFT SIDE */}
        <div className="contact-left">
          <h3>Get In Touch</h3>

          <p className="contact-text">
            Feel free to reach out to me for any opportunities, collaborations, or just to say hello!
          </p>

          <div className="contact-info">
            <p><FaEnvelope className="icon" /> nijbhavsar4433@gmail.com</p>
            <p><FaPhoneAlt className="icon" /> +91 9313234412</p>
            <p><FaMapMarkerAlt className="icon" /> Navsari, Gujarat, India</p>
          </div>

          <div className="social-icons">
            <a href="https://github.com/Nij-bhavsar"><FaGithub /></a>
            <a href="https://www.linkedin.com/in/nij-bhavsar-cse"><FaLinkedinIn /></a>
            <a href="https://www.instagram.com/the_nb.23?igsh=MWE4ZnpoY3M1bGUyeA=="><FaInstagram /></a>
            <a href="https://www.facebook.com/nij.bhavsar?rdid=UwsS78bYYhvNtBOF&share_url=https%3A%2F%2Fwww.facebook.com%2Fshare%2F1EN29v6Yu9%2F#"><FaFacebookF /></a>
          </div>
        </div>

        {/* RIGHT SIDE */}
        <div className="contact-right">
          <form>

            <input type="text" placeholder="Your Name" />
            <input type="email" placeholder="Your Email" />
            <input type="text" placeholder="Subject" />
            <textarea placeholder="Your Message"></textarea>

            <button type="submit">Send Message</button>

          </form>
        </div>

      </div>

    </section>
  );
};

export default Contact;