import React, { useEffect, useState } from "react";
import "../../App.scss";
import "./Woman.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const Woman = () => {
  const [models, setModels] = useState([]);

  useEffect(() => {
    const fetchModels = async () => {
      try {
        const response = await fetch(
          "https://modelagency-backend.onrender.com/models/women/?limit=12"
        );
        if (!response.ok) throw new Error("Failed to fetch models");

        const data = await response.json();
        setModels(data.results); // Загружаем модели из API
      } catch (error) {
        console.error("Error fetching models:", error);
      }
    };

    fetchModels();
  }, []);

  return (
    <>
      <div className="woman-page">
        <TopBar />

        <Link to="/search" className="top-bar__search-second">
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
        </Link>
      </div>

      <main className="main">
        <section className="our-models woman-models">
          <div className="our-models__title">
            <h2 className="our-models__title-text">Women</h2>
          </div>

          <Link to="/filter">
            <div className="filter">
              <div className="filter__text">Filter</div>
              <div>
                <img
                  src="/icons/man/icon-filter.svg"
                  alt="icon filter"
                  className="filter__icon"
                />
              </div>
            </div>
          </Link>

          <div className="our-models__block">
            {models.slice(0, 12).map((model, index) => (
              <Link
                to={`/models/women/${model.id}`}
                key={index}
                className="our-models__link"
              >
                <div className="our-models__card">
                  <div className="our-models__img">
                    <img
                      src={model.image_url}
                      alt={model.full_name || "Model"}
                    />
                  </div>
                  <div className="our-models__info">
                    <div className="our-models__name">
                      {model.full_name || "Loading..."}
                    </div>
                    <div className="our-models__location">
                      {model.city || "City"}, {model.country || "Country"}
                    </div>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
};

export default Woman;
