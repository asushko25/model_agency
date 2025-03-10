import React, { useState } from "react";
import "../../App.scss";
import TopBar from "../../components/TopBar/TopBar";
import Footer from "../../components/Footer/Footer";
import "./Contact.scss";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    last_name: "", 
    email: "", 
    phone_number: "", 
    message: "", 
    agreement: false, 
  });

  const isValidPhoneNumber = (phone) => {
    const phoneRegex = /^\+\d{7,15}$/;
    return phoneRegex.test(phone);
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    if (name === "phone_number") {
      setFormData({
        ...formData,
        [name]: value.replace(/\s/g, ""), 
      });
    } else {
      setFormData({
        ...formData,
        [name]: type === "checkbox" ? checked : value,
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); 

    if (!isValidPhoneNumber(formData.phone_number)) {
      alert(
        "Please enter a valid phone number with country code (e.g., +48234567489)."
      );
      return;
    }

    try {
      const response = await fetch("https://modelagency-backend.onrender.com/contact/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const result = await response.json().catch(() => null);

      if (response.ok) {
        alert("Form submitted successfully!");
        setFormData({
          name: "",
          last_name: "",
          email: "",
          phone_number: "",
          message: "",
          agreement: false,
        }); 
      } else {
        console.error("Request error:", result);
        alert(
          `Error: ${response.status} ${result ? JSON.stringify(result) : ""}`
        );
      }
    } catch (error) {
      console.error("Network error:", error);
      alert("Network error. Please check your server connection.");
    }
  };

  return (
    <>
      <div className="contact-page">
        <TopBar />
      </div>

      <main className="main main-contact">
        <section className="contact">
          <h1 className="contact-title">Contact us</h1>

          <div className="contact-content">
            <div className="contact-content__form">
              <form
                autoComplete="on"
                id="form"
                method="post"
                onSubmit={handleSubmit}
                className="contact__message-form"
              >
                <div className="contact__names">
                  <div className="user-name">
                    <label htmlFor="name" className="form__label">
                      Name*
                    </label>
                    <input
                      type="text"
                      id="name"
                      className="form__input form__input--name form__input-item"
                      name="name"
                      placeholder="Enter your name"
                      required
                      value={formData.name}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="company-name">
                    <label htmlFor="last_name" className="form__label">
                      Last name*
                    </label>
                    <input
                      type="text"
                      id="last_name"
                      className="form__input form__input--companyName form__input-item"
                      name="last_name"
                      placeholder="Enter your last name"
                      required
                      value={formData.last_name}
                      onChange={handleChange}
                    />
                  </div>
                </div>

                <div className="contact__info">
                  <div className="contact__email">
                    <label htmlFor="email" className="form__label">
                      Email*
                    </label>
                    <input
                      id="email"
                      className="form__input form__input--email"
                      type="email"
                      name="email"
                      placeholder="Enter your email"
                      required
                      value={formData.email}
                      onChange={handleChange}
                    />
                  </div>

                  <div className="contact__phone">
                    <label htmlFor="phone_number" className="form__label">
                      Phone number*
                    </label>
                    <input
                      id="phone_number"
                      className="form__input form__input--phone form__input-item"
                      type="tel"
                      name="phone_number"
                      placeholder="Enter your phone number"
                      required
                      value={formData.phone_number}
                      onChange={handleChange}
                    />
                  </div>
                </div>

                <div className="contact__message form__control">
                  <label htmlFor="message" className="form__label">
                    Message*
                  </label>
                  <textarea
                    name="message"
                    className="form__input input__textarea"
                    placeholder="Enter your message"
                    required
                    value={formData.message}
                    onChange={handleChange}
                  ></textarea>
                </div>

                <div className="contact__sent">
                  <div className="contact__policy">
                    <div className="contact-us__policy--text">
                      I agree to receive information from you by email regarding
                      your products and services*
                    </div>

                    <div className="contact__checkbox">
                      <label
                        htmlFor="checkbox"
                        className="contact__checkbox-label"
                      >
                        <input
                          className="check-box"
                          type="checkbox"
                          required
                          id="checkbox"
                          name="agreement"
                          checked={formData.agreement}
                          onChange={handleChange}
                        />
                        <span className="contact__checkbox-text">I agree</span>
                      </label>
                    </div>
                  </div>

                  <div className="contact__button">
                    <button className="contact__text" type="submit">
                      SUBMIT
                    </button>
                  </div>
                </div>
              </form>
            </div>

            <div className="contact-content__information">
              <div className="contact-content__information-photo">
                <img
                  src="./images/contact/contact-photo.png"
                  alt="contact-photo"
                />
              </div>
              <div className="contact-content__background"></div>
              <div className="contact-content__information-wrapper">
                <div className="contact-content__information-title">Axiom</div>
                <div className="contact-content__information-discription">
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
