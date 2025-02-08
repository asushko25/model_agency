import React from "react";
import TopBar from "../TopBar/TopBar";

const Header = () => {
  return (
    <header className="header">
      <div className="container header__container">
        <TopBar />
      </div>

      <a href="#search" className="top-bar__search-second">
        <div className="top-bar__search-container-second">
          <div className="top-bar__search-elements-second">
            <div className="top-bar__search-icon-second">
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

      <div className="header__title">Axiom</div>
      <div className="header__discription">
        Connect with top models worldwide. Effortless <br /> talent search to
        bring your vision to life.
      </div>
    </header>
  );
};

export default Header;
