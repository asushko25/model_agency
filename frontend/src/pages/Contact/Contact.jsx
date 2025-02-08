import React from "react";
import "../../App.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import "./Contact.scss";

const Contact = () => {
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
        <section className="contact">
          <h1 className="contact-title">Contact us</h1>

          <div className="contact-content">
            <div className="contact-content__form">
              <form
                autoComplete="on"
                id="form"
                action="#"
                method="post"
                onSubmit={(e) => {
                  e.preventDefault();
                  e.target.reset();
                }}
                className="contact__message-form"
              >
                <div className="contact__names">
                  <div className="user-name">
                    <label htmlFor="user-name" className="form__label">
                      Name*
                    </label>
                    <input
                      type="text"
                      id="user-name"
                      className="form__input form__input--name form__input-item"
                      name="user-name"
                      placeholder="Enter your name"
                      required
                    />
                  </div>

                  <div className="company-name">
                    <label htmlFor="last-name" className="form__label">
                      Last name*
                    </label>
                    <input
                      type="text"
                      id="last-name"
                      className="form__input form__input--companyName form__input-item"
                      name="last-name"
                      placeholder="Enter your last name"
                      required
                    />
                  </div>
                </div>

                <div className="contact__info">
                  <div className="contact__email">
                    <label htmlFor="user-email" className="form__label">
                      Email*
                    </label>
                    <input
                      id="user-email"
                      className="form__input form__input--email"
                      type="email"
                      name="email"
                      placeholder="Enter your email"
                      required
                    />
                  </div>

                  <div className="contact__phone">
                    <label htmlFor="user-phone" className="form__label">
                      Phone number*
                    </label>
                    <input
                      id="user-phone"
                      className="form__input form__input--phone form__input-item"
                      type="tel"
                      name="phone"
                      placeholder="Enter your phone number"
                      required
                    />
                  </div>
                </div>

                <div class="contact__message form__control">
                  <label htmlFor="user-message" className="form__label">
                    Massage*
                  </label>
                  <textarea
                    name="message"
                    class="form__input input__textarea"
                    placeholder="Enter your massage"
                    required
                  ></textarea>
                </div>

                <div class="contact__sent">
                  <div class="contact__policy">
                    <div class="contact-us__policy--text">
                      I agree to receive information from you by email regarding
                      your products and services*
                    </div>

                    <div class="contact__checkbox">
                      <label for="checkbox" class="contact__checkbox-label">
                        <input
                          class="check-box"
                          type="checkbox"
                          required
                          id="checkbox"
                        />
                        <span class="contact__checkbox-text">I agree</span>
                      </label>
                    </div>
                  </div>

                  <div class="contact__button">
                    <button class="contact__text" type="submit">
                      SUBMIT
                    </button>
                  </div>
                </div>
              </form>
            </div>

            <div class="contact-content__information">
              <div class="contact-content__information-photo">
                <img
                  src="./images/contact/contact-photo.png"
                  alt="contact-photo"
                />
              </div>
              <div className="contact-content__background"></div>
              <div class="contact-content__information-wrapper">
                <div class="contact-content__information-title">Axiom</div>
                <div class="contact-content__information-discription">
                  It is very important for us to keep in touch with you, so we
                  are always ready to answer any question that interests you.
                  Shoot!
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
};

export default Contact;
