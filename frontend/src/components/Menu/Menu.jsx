import React from "react";
import { Link } from "react-router-dom";
import "./Menu.scss";

const Menu = () => {
  return (
    <aside className="page__menu menu" id="menu">
      <div className="container">
        <div className="page__menu__content">
          <div className="aside-top-bar">
            <div className="top-bar__logo aside-top-bar__logo">
              <div className="top-bar__logo-main">Axiom</div>
              <div className="top-bar__logo-second aside-top-bar__logo-second">
                MODEL MANAGEMENT LLC
              </div>
            </div>

            <a href="#" className="icon--close">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
              >
                <path
                  d="M6 6L18 18"
                  stroke="#ECDFCC"
                  strokeWidth="2"
                  strokeLinecap="round"
                />
                <path
                  d="M18 6L6 18"
                  stroke="#ECDFCC"
                  strokeWidth="2"
                  strokeLinecap="round"
                />
              </svg>
            </a>
          </div>

          <div className="menu__content">
            <nav className="nav menu__nav">
              <ul className="aside-top-bar__list">
                <li className="aside-top-bar-item">
                  <Link to="/newsletter" className="aside-top-bar__link">
                    Newsletter
                  </Link>
                </li>
                <li className="aside-top-bar-item">
                  <Link to="/contact" className="aside-top-bar__link">
                    Contact
                  </Link>
                </li>
                <li className="aside-top-bar-item">
                  <Link to="/woman" className="aside-top-bar__link">
                    Women
                  </Link>
                </li>
                <li className="aside-top-bar-item">
                  <Link to="/man" className="aside-top-bar__link">
                    Man
                  </Link>
                </li>
              </ul>
            </nav>
          </div>
        </div>

        <div className="menu__socials">
          <a href="https://web.telegram.org/k/">
            <img src="./icons/footer/telegram.svg" alt="Telegram Logo" />
          </a>
          <a href="https://www.instagram.com/">
            <img src="./icons/footer/instagram.svg" alt="Instagram Logo" />
          </a>
          <a href="https://www.facebook.com/">
            <img src="./icons/footer/facebook.svg" alt="Facebook Logo" />
          </a>
        </div>
      </div>
    </aside>
  );
};

export default Menu;
