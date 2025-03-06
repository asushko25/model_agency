import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer__container footer-error">
        <div className="footer__logo">
          <div className="footer__logo-main top-bar__logo-main">Axiom</div>
          <div className="footer__logo-second top-bar__logo-second">
            MODEL MANAGEMENT LLC
          </div>
        </div>

        <div className="footer__terms">
          <Link to="/terms-of-service" className="footer__terms-text">
            Terms
          </Link>
          <span className="footer__terms-element">|</span>
          <Link to="/privacy-policy" className="footer__terms-text">
            Privacy
          </Link>
        </div>

        <div className="footer__socials">
          <a
            href="https://web.telegram.org/k/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img src="/icons/footer/telegram.svg" alt="Telegram Logo" />
          </a>

          <a
            href="https://www.instagram.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img src="/icons/footer/instagram.svg" alt="Instagram Logo" />
          </a>

          <a
            href="https://www.facebook.com/"
            target="_blank"
            rel="noopener noreferrer"
          >
            <img src="/icons/footer/facebook.svg" alt="Facebook Logo" />
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
