import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React, { useState, useEffect } from "react";
import Menu from "../components/Menu/Menu";
import OurModels from "../components/OurModels/OurModels";
import Man from "../pages/Man/Man";
import Woman from "../pages/Woman/Woman";
import Error from "../pages/Error/Error";
import Contact from "../pages/Contact/Contact";
import Newsletter from "../pages/Newsletter/Newsletter";
import NewsletterMain from "../pages/NewsletterMain/NewsletterMain";
import Person from "../pages/Person/Person";
import Search from "../pages/Search/Search";

function Root() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  useEffect(() => {
    if (isMenuOpen) {
      document.body.classList.add("menu-open");
    } else {
      document.body.classList.remove("menu-open");
    }
  }, [isMenuOpen]);

  const toggleMenu = () => {
    setIsMenuOpen((prev) => !prev);
  };

  return (
    <div className={`App ${isMenuOpen ? "menu-active" : ""}`}>
      <div className="wrapper">
        <Menu isOpen={isMenuOpen} toggleMenu={toggleMenu} />
        <Routes>
          <Route path="/" element={<OurModels />} />
          <Route path="/man" element={<Man />} />
          <Route path="/woman" element={<Woman />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/newsletter-sign" element={<Newsletter />} />
          <Route path="/newsletter" element={<NewsletterMain />} />
          <Route path="/models/men/:id" element={<Person />} />
          <Route path="/models/women/:id" element={<Person />} />
          <Route path="/models/main/:id" element={<Person />} />
          <Route path="/menu" element={<Menu />} />
          <Route path="/search" element={<Search />} />
          <Route path="*" element={<Error />} />
        </Routes>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <Root />
    </Router>
  );
}
