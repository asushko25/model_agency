import React, { useEffect, useState } from "react";
import "./OurModels.scss";
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import { Link } from "react-router-dom";

const OurModels = () => {
  const [models, setModels] = useState([]);
  const [showMore, setShowMore] = useState(false);

  useEffect(() => {
    const fetchModels = async () => {
      try {
        const response = await fetch(
          "https://modelagency-backend.onrender.com/models/main/?limit=12"
        );
        if (!response.ok) throw new Error("Failed to fetch models");

        const data = await response.json();
        setModels(data.results);
      } catch (error) {
        console.error("Error fetching models:", error);
      }
    };

    fetchModels();
  }, []);

  return (
    <>
      <Header />

      <main className="main">
        <section className="our-models__introdusing">
          <div className="our-models__introdusing-left">
            <div className="our-models__introdusing-left__text">
              At Axiom, we believe every model has a unique story. Whether
              you're just starting or an experienced professional, we offer
              personalized guidance and connect you with top clients across
              fashion, advertising, and commercial industries to help you grow
              and succeed.
            </div>

            <div className="our-models__introdusing-left__img">
              <img
                src="/images/our-models/introduce-left.png"
                alt="introduce model"
              />
            </div>
          </div>

          <div className="our-models__introdusing-center">
            <div className="our-models__introdusing-center__img">
              <img
                src="/images/our-models/introduce-center.png"
                alt="introduce model"
              />
            </div>
          </div>

          <div className="our-models__introdusing-right">
            <div className="our-models__introdusing-right__img">
              <img
                src="/images/our-models/introduce-right.png"
                alt="introduce model"
              />
            </div>

            <div className="our-models__introdusing-right__text">
              Welcome to Axiom Models – where beauty, talent, and
              professionalism come together to create a new standard in the
              modeling industry. We are more than just an agency; we are a
              creative powerhouse, committed to shaping the future of fashion
              and modeling.
            </div>
          </div>
        </section>

        <section className="our-models">
          <div className="our-models__title">
            <h2 className="our-models__title-text">
              Connect with our top models worldwide. Effortless talent search to
              bring your vision to life.
            </h2>
          </div>

          <div className="our-models__block">
            {models.slice(0, 6).map((model, index) => (
              <Link
                to={`/models/main/${model.id}`}
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

          {showMore && (
            <div className="our-models__block our-models__block-third">
              {models.slice(6, 12).map((model, index) => (
                <Link
                  to={`/models/main/${model.id}`}
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
          )}

          {!showMore && models.length > 6 && (
            <div className="our-models__btn">
              <div
                className="our-models__btn-show"
                onClick={() => setShowMore(true)}
              >
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
