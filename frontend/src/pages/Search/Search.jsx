import React, { useEffect, useState, memo } from "react";
import "../../App.scss";
import "./Search.scss";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const ModelCard = memo(({ model }) => (
  <Link to={`/models/main/${model.id}`} className="our-models__link">
    <div className="our-models__card">
      <div className="our-models__img">
        <img src={model.image_url} alt={model.full_name || "Model"} />
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
));

const Search = () => {
  const [models, setModels] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [debouncedSearchTerm, setDebouncedSearchTerm] = useState("");
  const [showNotFound, setShowNotFound] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [page, setPage] = useState(1);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedSearchTerm(searchTerm);
      setPage(1);
    }, 1500);

    return () => {
      clearTimeout(handler);
      setShowNotFound(false);
    };
  }, [searchTerm]);

  useEffect(() => {
    const fetchModels = async () => {
      try {
        if (debouncedSearchTerm.trim() !== "") {
          setIsLoading(true);
          const response = await fetch(
            `https://modelagency-backend.onrender.com/models/main/?search=${debouncedSearchTerm}&limit=9&offset=${
              (page - 1) * 9
            }`
          );
          if (!response.ok) throw new Error("Failed to fetch models");

          const data = await response.json();
          setModels((prevModels) =>
            page === 1 ? data.results : [...prevModels, ...data.results]
          );
          setShowNotFound(data.results.length === 0);
        } else {
          setModels([]);
        }
      } catch (error) {
        console.error("Error fetching models:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchModels();
  }, [debouncedSearchTerm, page]);

  const loadMore = () => setPage((prev) => prev + 1);

  return (
    <>
      <div className="search-page">
        <div className="top-bar">
          <div className="top-bar__navigation top-bar__navigation-person">
            <nav className="top-bar__nav top-bar__nav-person">
              <ul className="top-bar__list top-bar__list-person">
                <li className="top-bar__item top-bar__item-person">
                  <Link to="/woman" className="top-bar__link">
                    Women
                  </Link>
                </li>
                <li className="top-bar__item top-bar__item-person">
                  <Link to="/man" className="top-bar__link">
                    Man
                  </Link>
                </li>
                <li className="top-bar__item top-bar__item-person">
                  <Link to="/newsletter" className="top-bar__link">
                    Newsletter
                  </Link>
                </li>
                <li className="top-bar__item top-bar__item-contact top-bar__item-person">
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

          <li className="top-bar__item top-bar__item__left top-bar__item__search">
            <Link to="/">
              <div className="top-bar__person-info__left-item top-bar__person-info__left-search">
                <img src="/icons/person/icon-close.svg" alt="icon-close" />
              </div>
            </Link>
          </li>

          <button type="button" className="btn--mobile-nav">
            <a href="#menu">
              <img src="/icons/header/burger-menu.svg" alt="burger-menu" />
            </a>
          </button>
        </div>

        <div className="top-bar__search-container-second top-bar__search-container-second__search">
          <div className="top-bar__search-elements-second">
            <div className="top-bar__search-icon-second">
              <img
                src="/icons/header/search.svg"
                alt="search"
                className="top-bar__search-item"
              />
            </div>
            <input
              type="text"
              placeholder="Search Model"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="top-bar__search-input"
            />
          </div>
        </div>

        <main className="main">
          <section className="our-models man-models">
            <div className="our-models__block our-models__block-results">
              {isLoading && <div className="loader">Loading...</div>}
              {models.length > 0
                ? models.map((model) => (
                    <ModelCard key={model.id} model={model} />
                  ))
                : showNotFound && (
                    <p className="no-results">No results found</p>
                  )}
            </div>

            {!isLoading && models.length > 0 && (
              <div className="our-models__btn">
                <div className="our-models__btn-show" onClick={loadMore}>
                  Load More
                </div>
              </div>
            )}
          </section>
        </main>
      </div>

      <Footer />
    </>
  );
};

export default Search;
