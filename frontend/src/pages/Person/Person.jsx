import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import "../../App.scss";
import "./Person.scss";
import Footer from "../../components/Footer/Footer";

const Person = () => {
  let { category, id } = useParams();
  const [model, setModel] = useState(null);
  const [loading, setLoading] = useState(true);

  if (!["main", "men", "women"].includes(category)) {
    category = "main";
  }

  useEffect(() => {
    const fetchModel = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/models/${category}/${id}/`
        );
        if (!response.ok) throw new Error("Failed to fetch model");

        const data = await response.json();
        setModel(data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching model:", error);
        setLoading(false);
      }
    };

    fetchModel();
  }, [category, id]);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (!model) {
    return <div className="error">Model not found</div>;
  }

  return (
    <>
      <div className="person-page">
        <div className="top-bar">
          <div className="top-bar__navigation top-bar__navigation-person">
            <nav className="top-bar__nav top-bar__nav-person">
              <ul className="top-bar__list top-bar__list-person">
                <li className="top-bar__item top-bar__item__left">
                  <Link to="/">
                    <div className="top-bar__person-info__left-item">
                      <img
                        src="/icons/person/icon-close.svg"
                        alt="icon-close"
                      />
                    </div>
                  </Link>
                </li>

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

          <a href="/search" className="top-bar__search">
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
        <section className="person-info">
          <Link to="/">
            <div className="person-info__left">
              <img src="/icons/person/icon-close.svg" alt="icon-close" />
            </div>
          </Link>

          <div className="person-info__photo">
            {model.images && model.images.length > 0 ? (
              <img src={model.images[0].image} alt={`Model ${model.id}`} />
            ) : (
              <p>No image available</p>
            )}
          </div>

          <div className="person-info__right">
            <div className="person-info__parameters">
              <div className="person-info__item person-info__height">
                HEIGHT: {model.height || "N/A"}
              </div>
              <div className="person-info__item person-info__eyes">
                EYES: {model.eye_color || "N/A"}
              </div>
              <div className="person-info__item person-info__shoes">
                WAIST: {model.waist || "N/A"}
              </div>
              <div className="person-info__item person-info__bust">
                BUST: {model.bust || "N/A"}
              </div>
              <div className="person-info__item person-info__hips">
                HIPS: {model.hips || "N/A"}
              </div>
              <div className="person-info__item person-info__waist">
                WAIST: {model.waist || "N/A"}
              </div>

              <div className="person-info__pages">
                <Link
                  to="/contact"
                  className="top-bar__link top-bar__link-contactPerson"
                >
                  Contact
                </Link>
              </div>
            </div>
          </div>

          <div>
            <div className="person-info__pages person-info__pages-mobile">
              <Link
                to="/contact"
                className="top-bar__link top-bar__link-contactPerson"
              >
                Contact
              </Link>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
};

export default Person;
