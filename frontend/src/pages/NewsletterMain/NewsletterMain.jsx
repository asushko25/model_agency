import React from "react";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import "./NewsletterMain.scss";

const NewsletterMain = () => {
  return (
    <>
      <div className="contact-page">
        <TopBar />

        <a
          href="#search"
          className="top-bar__search-second contact__search-second "
        >
          <div className="top-bar__search-container-second contact__search-second">
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
      </div>

      <main className="main main-contact">
        <section className="newsletter">
          <div className="newsletter__wrapper">
            <h1 className="newsletter__title">Newsletter</h1>

            <div className="newsletter__block">
              <div className="newsletter__block-left">
                <div className="newsletter__block-title">
                  Model Salaries on the Rise in 2024
                </div>

                <div className="newsletter__block-photo">
                  <img
                    src="/images/newsletter/first.png"
                    alt="Model Salaries"
                  />
                </div>

                <div className="newsletter__block-discription">
                  The modeling industry is experiencing a pay increase for top
                  models in 2024, thanks to a surge in demand for digital
                  influencers and fashion collaborations. Find out how much top
                  models are making in the current market!
                </div>
              </div>

              <div className="newsletter__block-right">
                <div className="newsletter__block-title">
                  International Expansion: Models Wanted for Global Campaigns
                </div>

                <div className="newsletter__block-photo">
                  <img
                    src="/images/newsletter/second.png"
                    alt="International Expansion"
                  />
                </div>

                <div className="newsletter__block-discription">
                  Global brands like Chanel and Nike are expanding their search
                  for models from emerging markets such as India, Africa, and
                  Latin America. This opens up exciting new opportunities for
                  models to break into international campaigns.
                </div>
              </div>
            </div>
            <div className="newsletter__block">
              <div className="newsletter__block-left">
                <div className="newsletter__block-title">
                  Fashion Week 2024: New Faces on the Runway
                </div>

                <div className="newsletter__block-photo">
                  <img
                    src="/images/newsletter/third.png"
                    alt="Model Salaries"
                  />
                </div>

                <div className="newsletter__block-discription">
                  Fashion Week 2024 is set to introduce a record number of
                  first-time models on the runway. Designers are breaking away
                  from traditional beauty standards, and we're seeing more
                  diversity and fresh talent than ever before.
                </div>
              </div>

              <div className="newsletter__block-right">
                <div className="newsletter__block-title">
                  Sustainability in Modeling: The New Trend
                </div>

                <div className="newsletter__block-photo">
                  <img
                    src="/images/newsletter/fourth.png"
                    alt="International Expansion"
                  />
                </div>

                <div className="newsletter__block-discription">
                  Eco-conscious fashion is not just for designers — the modeling
                  industry is jumping on the sustainability bandwagon. Agencies
                  are now partnering with eco-friendly brands and offering
                  models opportunities to work on environmentally conscious
                  campaigns.
                </div>
              </div>
            </div>

            <div className="newsletter__block">
              <div className="newsletter__block-left">
                <div className="newsletter__block-title">
                  Top Model’s Career Shift: From Runway to Creative Director
                </div>

                <div className="newsletter__block-photo">
                  <img
                    src="/images/newsletter/fifth.png"
                    alt="Model Salaries"
                  />
                </div>

                <div className="newsletter__block-discription">
                  Gigi Hadid has recently made the switch from model to creative
                  director for a leading brand, proving that the modeling
                  industry offers many career paths beyond the runway. Is this
                  the future for other top models?
                </div>
              </div>

              <div className="newsletter__block-right">
                <div className="newsletter__block-title">
                  The Rise of Digital Models
                </div>

                <div className="newsletter__block-photo">
                  <img
                    src="/images/newsletter/six.png"
                    alt="International Expansion"
                  />
                </div>

                <div className="newsletter__block-discription">
                  In the world of virtual fashion, digital models like Lil
                  Miquela are becoming just as influential as their real-life
                  counterparts. Discover how digital models are being used in
                  advertising and campaigns, and what this means for the future
                  of modeling.
                </div>
              </div>
            </div>
          </div>
        </section>
        <div className="join-newsletter__title">
          about the latest model castings, exclusive opportunities, and upcoming
          collaborations!
        </div>

        <a href="/newsletter-sign">
          <div className="our-models__btn-show join-newsletter__button">
            JOIN THE NEWSLETTER
          </div>
        </a>

        <div className="newsletter-navigation">
          <div className="newsletter-navigation__left">
            <a href="/error">
              <img src="/images/newsletter/icon-left.svg" alt="icon-left" />
            </a>
          </div>

          <div className="newsletter-navigation__items">
            <div className="newsletter-navigation__item">
              <a className="newsletter-navigation__link" href="/error">
                1
              </a>
            </div>

            <div className="newsletter-navigation__item">
              <a className="newsletter-navigation__link" href="/error">
                2
              </a>
            </div>

            <div className="newsletter-navigation__item">
              <a className="newsletter-navigation__link" href="/error">
                3
              </a>
            </div>
          </div>

          <div className="newsletter-navigation__right">
            <a href="/error">
              <img src="/images/newsletter/icon-right.svg" alt="icon-right" />
            </a>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
};

export default NewsletterMain;
