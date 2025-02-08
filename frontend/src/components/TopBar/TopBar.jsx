
import React from "react";
import { Link } from "react-router-dom";

const TopBar = () => {
  return (
    <div className="top-bar">
      <div className="top-bar__navigation">
        <nav className="top-bar__nav">
          <ul className="top-bar__list">
            <li className="top-bar__item">
              <Link to="/woman" className="top-bar__link">
                Women
              </Link>
            </li>
            <li className="top-bar__item">
              <Link to="/man" className="top-bar__link">
                Man
              </Link>
            </li>
            <li className="top-bar__item">
              <Link to="/newsletter" className="top-bar__link">
                Newsletter
              </Link>
            </li>
            <li className="top-bar__item top-bar__item-contact">
              <Link to="/contact" className="top-bar__link">
                Contact
              </Link>
            </li>
          </ul>
        </nav>
      </div>

      <div className="top-bar__logo">
        <div className="top-bar__logo-main">Axiom</div>
        <div className="top-bar__logo-second">MODEL MANAGEMENTLLC</div>
      </div>

      <a href="#search" className="top-bar__search">
        <div className="top-bar__search-container">
          <div className="top-bar__search-elements">
            <div className="top-bar__search-icon">
              <img
                src="/icons/header/search.svg"
                alt="search"
                className="top-bar__search-item"
              />
            </div>
            <div className="top-bar__search-text">Search Model</div>
          </div>
        </div>
      </a>

      <button type="button" className="btn--mobile-nav">
        <a href="#menu">
          <img src="/icons/header/burger-menu.svg" alt="burger-menu" />
        </a>
      </button>
    </div>
  );
};

export default TopBar;
