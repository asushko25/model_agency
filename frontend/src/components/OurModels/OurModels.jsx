import React, { useEffect, useState } from "react";

import "./OurModels.scss";
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import { Link } from "react-router-dom";

const OurModels = () => {
  const [models, setModels] = useState([]); // Список моделей

  // Загружаем данные с сервера
  useEffect(() => {
    const fetchModels = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/models/main/");
        if (!response.ok) throw new Error("Failed to fetch models");

        const data = await response.json();
        setModels(data.results); // Устанавливаем модели из API
      } catch (error) {
        console.error("Error fetching models:", error);
      }
    };

    fetchModels();
  }, []);

  const [showMore, setShowMore] = useState(false);

  const handleShowMore = () => {
    setShowMore(true);
  };

  return (
    <>
      <Header />

      <section className="about">
        <div className="about__image--left">
          <img src="/images/our-models/left.png" alt="left" />
        </div>

        <div className="about__image--center">
          <img src="/images/our-models/center.png" alt="left" />
        </div>

        <div className="about__image--right">
          <img src="/images/our-models/right.png" alt="right" />
        </div>
      </section>

      <main className="main">
        <section className="our-models">
          <div className="our-models__title">
            <h2 className="our-models__title-text">
              Connect with our top models worldwide. Effortless talent search
              <br /> to bring your vision to life.
            </h2>
          </div>

          <div className="our-models__block">
            <Link
              to={models[0]?.detail_url || "/"}
              className="our-models__link"
            >
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src={models[0]?.image_url}
                    alt={models[0]?.full_name || "Model"}
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">
                    {models[0]?.full_name || "Loading..."}
                  </div>
                  <div className="our-models__location">
                    {models[0]?.city || "City"},{" "}
                    {models[0]?.country || "Country"}
                  </div>
                </div>
              </div>
            </Link>

            <Link
              to={models[0]?.detail_url || "/"}
              className="our-models__link"
            >
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src={models[1]?.image_url}
                    alt={models[1]?.full_name || "Model"}
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">
                    {models[1]?.full_name || "Loading..."}
                  </div>
                  <div className="our-models__location">
                    {models[1]?.city || "City"},{" "}
                    {models[1]?.country || "Country"}
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" href="#model-jay" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/our-models/model-edle.png"
                    alt="Karlie Kloss"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Karlie Kloss</div>
                  <div className="our-models__location">
                    Copenhagen, Denmark
                  </div>
                </div>
              </div>
            </Link>
          </div>

          <div className="our-models__block our-models__block-second">
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/our-models/bella-hadid.png"
                    alt="Bella Hadid"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Bella Hadid</div>
                  <div className="our-models__location">
                    United States, Los Angeles
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/our-models/gigi-hadid.png"
                    alt="Gigi Hadid"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Gigi Hadid</div>
                  <div className="our-models__location">Tokyo, Japan</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/our-models/kendall-jenner.png"
                    alt="Kendall Jenner"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Kendall Jenner</div>
                  <div className="our-models__location">
                    United States, Los Angeles
                  </div>
                </div>
              </div>
            </Link>
          </div>

          {showMore && (
            <>
              <div className="our-models__block our-models__block-third">
                <Link to="/person" className="our-models__link">
                  <div className="our-models__card">
                    <div className="our-models__img">
                      <img
                        src="/images/our-models/model-jay.png"
                        alt="Naomi Campbell"
                      />
                    </div>
                    <div className="our-models__info">
                      <div className="our-models__name">Naomi Campbell</div>
                      <div className="our-models__location">
                        London, United Kingdom
                      </div>
                    </div>
                  </div>
                </Link>

                <Link to="/person" className="our-models__link">
                  <div className="our-models__card">
                    <div className="our-models__img">
                      <img
                        src="/images/our-models/model-shouta.png"
                        alt="Kate Moss"
                      />
                    </div>
                    <div className="our-models__info">
                      <div className="our-models__name">Kate Moss</div>
                      <div className="our-models__location">Tokyo, Japan</div>
                    </div>
                  </div>
                </Link>

                <Link to="/person" className="our-models__link">
                  <div className="our-models__card">
                    <div className="our-models__img">
                      <img
                        src="/images/our-models/model-edle.png"
                        alt="Karlie Kloss"
                      />
                    </div>
                    <div className="our-models__info">
                      <div className="our-models__name">Karlie Kloss</div>
                      <div className="our-models__location">
                        Copenhagen, Denmark
                      </div>
                    </div>
                  </div>
                </Link>
              </div>

              <div className="our-models__block our-models__block-fourth">
                <Link to="/person" className="our-models__link">
                  <div className="our-models__card">
                    <div className="our-models__img">
                      <img
                        src="/images/our-models/bella-hadid.png"
                        alt="Bella Hadid"
                      />
                    </div>
                    <div className="our-models__info">
                      <div className="our-models__name">Bella Hadid</div>
                      <div className="our-models__location">
                        United States, Los Angeles
                      </div>
                    </div>
                  </div>
                </Link>

                <Link to="/person" className="our-models__link">
                  <div className="our-models__card">
                    <div className="our-models__img">
                      <img
                        src="/images/our-models/gigi-hadid.png"
                        alt="Gigi Hadid"
                      />
                    </div>
                    <div className="our-models__info">
                      <div className="our-models__name">Gigi Hadid</div>
                      <div className="our-models__location">Tokyo, Japan</div>
                    </div>
                  </div>
                </Link>

                <Link to="/person" className="our-models__link">
                  <div className="our-models__card">
                    <div className="our-models__img">
                      <img
                        src="/images/our-models/kendall-jenner.png"
                        alt="Kendall Jenner"
                      />
                    </div>
                    <div className="our-models__info">
                      <div className="our-models__name">Kendall Jenner</div>
                      <div className="our-models__location">
                        United States, Los Angeles
                      </div>
                    </div>
                  </div>
                </Link>
              </div>
            </>
          )}

          {!showMore && (
            <div className="our-models__btn">
              <div className="our-models__btn-show" onClick={handleShowMore}>
                Show more
              </div>
            </div>
          )}
        </section>
      </main>
      <Footer />
    </>
  );
};

export default OurModels;
