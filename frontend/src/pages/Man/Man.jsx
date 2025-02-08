import React from "react";
import "../../App.scss";
import "./Man.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const Man = () => {
  return (
    <>
      <div className="man-page">
        <TopBar />
      </div>

      <main className="main">
        <section className="our-models man-models">
          <div className="our-models__title">
            <h2 className="our-models__title-text">Man</h2>
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
                  <img src="/images/man/sean.png" alt="Sean O'Pry" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Sean O'Pry</div>
                  <div className="our-models__location">
                    United States, New York City
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/gandy.png" alt="David Gandy" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">David Gandy</div>
                  <div className="our-models__location">
                    United Kingdom, London
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/man/kortajarena.png"
                    alt="Jon Kortajarena"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Jon Kortajarena</div>
                  <div className="our-models__location">Spain, Barcelona</div>
                </div>
              </div>
            </Link>
          </div>

          <div className="our-models__block our-models__block-second">
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/nessman.png" alt="Simon Nessman" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Simon Nessman</div>
                  <div className="our-models__location">Canada, Vancouver</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/smith.png" alt="Lucky Blue Smith" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Lucky Blue Smith</div>
                  <div className="our-models__location">
                    United States, Los Angeles
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/beckford.png" alt="Tyson Beckford" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Tyson Beckford</div>
                  <div className="our-models__location">
                    United States, New York City
                  </div>
                </div>
              </div>
            </Link>
          </div>

          <div className="our-models__block our-models__block-third">
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img
                    src="/images/man/chabernaud.png"
                    alt="Clement Chabernaud"
                  />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Clement Chabernaud</div>
                  <div className="our-models__location">France, Paris</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/paulo.png" alt="Marlon Teixeira" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Marlon Teixeira</div>
                  <div className="our-models__location">Brazil, São Paulo</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/boselli.png" alt="Pietro Boselli" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Pietro Boselli</div>
                  <div className="our-models__location">Italy, Milan</div>
                </div>
              </div>
            </Link>
          </div>

          <div className="our-models__block our-models__block-fourth">
            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/pejić.png" alt="Andrej Pejić" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Andrej Pejić</div>
                  <div className="our-models__location">
                    Bosnia and Herzegovina, Melbourne
                  </div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/mills.png" alt="Noah Mills" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Noah Mills</div>
                  <div className="our-models__location">Canada, Toronto</div>
                </div>
              </div>
            </Link>

            <Link to="/person" className="our-models__link">
              <div className="our-models__card">
                <div className="our-models__img">
                  <img src="/images/man/hemsworth.png" alt="Chris Hemsworth" />
                </div>
                <div className="our-models__info">
                  <div className="our-models__name">Chris Hemsworth</div>
                  <div className="our-models__location">
                    Australia, Melbourne
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

export default Man;
