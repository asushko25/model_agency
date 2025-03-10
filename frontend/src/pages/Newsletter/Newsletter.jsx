import React from "react";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import "./Newsletter.scss";
import { Link } from "react-router-dom";

const Newsletter = () => {
  const handleSubmit = async (e) => {
    e.preventDefault();

    const emailInput = e.target.elements["user-email"].value.trim(); 

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput)) {
      alert("Please enter a valid email address.");
      return;
    }

    try {
      const response = await fetch("https://modelagency-backend.onrender.com/newsletters/sign/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: emailInput }),
      });

      if (response.ok) {
        alert("Successfully subscribed to the newsletter!");
        e.target.reset(); 
      } else {
        alert("Subscription failed. Please try again.");
      }
    } catch (error) {
      alert("Network error. Please check your connection.");
    }
  };

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

            <div className="newsletter__discription">
              Sign up for newsletters below. Just tell us which newsletters you
              want to receive and where to send them.
            </div>
          </div>

          <form
            autoComplete="on"
            id="form"
            onSubmit={handleSubmit}
            className="newsletter__message-form"
          >
            <div className="newsletter__main">
              <div className="newsletter__main-left">
                <div className="newsletter__items">
                  <div className="newsletter__item">
                    <div className="newsletter__checkbox">
                      <label
                        htmlFor="checkbox"
                        className="newsletter__checkbox-label"
                      >
                        <input
                          className="check-box check-box__newsletter"
                          type="checkbox"
                          id="checkbox"
                        />
                      </label>

                      <div className="newsletter__checkbox-text">
                        <div className="newsletter__checkbox-title">
                          Personalized Recommendations
                        </div>

                        <div className="newsletter__checkbox-discription">
                          1-3 emails/week
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="newsletter__item">
                    <div className="newsletter__checkbox">
                      <label
                        htmlFor="checkbox"
                        className="newsletter__checkbox-label"
                      >
                        <input
                          className="check-box check-box__newsletter"
                          type="checkbox"
                          id="checkbox"
                        />
                      </label>

                      <div className="newsletter__checkbox-text">
                        <div className="newsletter__checkbox-title">
                          ModelVibe{" "}
                        </div>

                        <div className="newsletter__checkbox-discription">
                          1 email/week
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="newsletter__item">
                    <div className="newsletter__checkbox">
                      <label
                        htmlFor="checkbox"
                        className="newsletter__checkbox-label"
                      >
                        <input
                          className="check-box check-box__newsletter"
                          type="checkbox"
                          id="checkbox"
                        />
                      </label>

                      <div className="newsletter__checkbox-text">
                        <div className="newsletter__checkbox-title">
                          ModelVibe Newsletter
                        </div>

                        <div className="newsletter__checkbox-discription">
                          3 emails/week
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="newsletter__item">
                    <div className="newsletter__checkbox">
                      <label
                        htmlFor="checkbox"
                        className="newsletter__checkbox-label"
                      >
                        <input
                          className="check-box check-box__newsletter"
                          type="checkbox"
                          id="checkbox"
                        />
                      </label>

                      <div className="newsletter__checkbox-text">
                        <div className="newsletter__checkbox-title">
                          Trending on ModelVibe
                        </div>

                        <div className="newsletter__checkbox-discription">
                          1-3 emails/week
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div className="newsletter__main-line"></div>

              <div className="newsletter__main-right">
                <div className="contact__email">
                  <label
                    htmlFor="user-email"
                    className="form__label form__label-newsletter"
                  >
                    Email
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

                <div className="newsletter__main-right-text">
                  By submitting your email address, you're agreeing to let us
                  send you customized marketing messages about us and our
                  advertising partners. You are also agreeing to our{" "}
                  <Link to="/terms-of-service" className="newsletter__link">
                    Terms of Service
                  </Link>
                  and{" "}
                  <Link to="/privacy-policy" className="newsletter__link">
                    Privacy Policy
                  </Link>
                  .
                </div>

                <div className="contact__button newsletter__button">
                  <button
                    className="contact__text newsletter__text"
                    type="submit"
                  >
                    SUBMIT
                  </button>
                </div>
              </div>
            </div>
          </form>
        </section>
      </main>
      <Footer />
    </>
  );
};

export default Newsletter;
