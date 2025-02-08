import React from "react";
import { Link } from "react-router-dom";
import "../../App.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import "./Error.scss";

const Error = () => {
  return (
    <div className="error-page">
      <div className="error-page__content">
        <TopBar />
        <div className="error-page__title">Oops...</div>
        <div className="error-page__description">
          The page you were looking for doesn't exist.
        </div>
        <Link to="/">
          <div className="error-page__btn">
            <div className="error-page__btn-show">GO BACK</div>
          </div>
        </Link>
        <Footer />
      </div>
    </div>
  );
};

export default Error;
