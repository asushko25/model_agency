import React from "react";
import "../../App.scss";
import "./Woman.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const Woman = () => {
  return (
    <>
      <div className="woman-page">
        <TopBar />
      </div>

      <main className="main">
        <section className="our-models man-models">
          <div className="our-models__title">
            <h2 className="our-models__title-text">Woman</h2>
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
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/garn.png" alt="Toni Garrn" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">SToni Garrn</div>
                  <div className="our-models__location">
                    London, United Kindom
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/sampaio.png" alt="Sara Sampaio" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Sara Sampaio</div>
                  <div className="our-models__location">Tokyo, Japan</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/jenner.png" alt="Kendall Jenner" />
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

          <div className="our-models__block our-models__block-second">
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/bella-hadid.png" alt="Bella Hadid" />
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
                  <img src="/images/woman/gigi-hadid.png" alt="Gigi Hadid" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Gigi Hadid</div>
                  <div className="our-models__location">
                    United States, New York City
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/kendal.png" alt="Kendall Jenner" />
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

          <div className="our-models__block our-models__block-third">
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/palvin.png" alt="Barbara Palvin" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Barbara Palvin</div>
                  <div className="our-models__location">Hungary, Budapest</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/dunn.png" alt="Jourdan Dunn" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Jourdan Dunn</div>
                  <div className="our-models__location">
                    United Kingdom, London
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/bruna.png" alt="Cindy Bruna" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Cindy Bruna</div>
                  <div className="our-models__location">IFrance, Paris</div>
                </div>
              </div>
            </Link>
          </div>

          <div className="our-models__block our-models__block-fourth">
            <Link to="/person"className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/woman/kocianova.png"
                    alt="Michaela Kocianova"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Michaela Kocianova</div>
                  <div className="our-models__location">
                    Slovakia, Bratislava
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/woman/fowler.png" alt="Georgia Fowler" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Georgia Fowler</div>
                  <div className="our-models__location">
                    New Zealand, Auckland
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/woman/swanepoel.png"
                    alt="Candice Swanepoel"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Candice Swanepoel</div>
                  <div className="our-models__location">
                    South Africa, Cape Town
                  </div>
                </div>
              </div>
            </Link>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
};

export default Woman;
