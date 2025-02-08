import React from "react";
import "../../App.scss";
import "./Person.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const Person = () => {
  return (
    <>
      <div className="person-page">
        <TopBar />
      </div>

      <main className="main">
        <section className="person-info">
          <Link to="/">
            <div className="person-info__left">
              <img src="/icons/person/icon-close.svg" alt="icon-close" />
            </div>
          </Link>

          <div className="person-info__photo">
            <img src="/images/person/model.png" alt="model" />
          </div>

          <div className="person-info__right">
            <div className="person-info__parameters">
              <div className="person-info__item person-info__height">
                HEIGHT 5’11 ””
              </div>
              <div className="person-info__item person-info__eyes">
                EYES Brown
              </div>
              <div className="person-info__item person-info__shoes">
                SHOES 9 1/2
              </div>
              <div className="person-info__item person-info__bust">
                BUST 30 1/2
              </div>
              <div className="person-info__item person-info__hips">
                HIPS 34 1/2
              </div>
              <div className="person-info__item person-info__waist">
                WAIST 23
              </div>

              <div className="person-info__pages">
                <div className="person-info__pages-left">
                  <img src="/icons/person/left.svg" alt="icon left" />
                </div>

                <div className="person-info__pages-numbers">1/16</div>

                <div className="person-info__pages-right">
                  <img src="/icons/person/right.svg" alt="icon right" />
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

export default Person;
