import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import React, { useState } from "react";
import Menu from "../components/Menu/Menu";
import OurModels from "../components/OurModels/OurModels";
import Man from "../pages/Man/Man";
import Woman from "../pages/Woman/Woman";
import Error from "../pages/Error/Error";
import Contact from "../pages/Contact/Contact";
import Newsletter from "../pages/Newsletter/Newsletter";
import NewsletterMain from "../pages/NewsletterMain/NewsletterMain";
import Person from "../pages/Person/Person";

function Root() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen((prev) => !prev);
  };

  return (
    <div className="App">
      <div className="wrapper">
        <Menu isOpen={isMenuOpen} toggleMenu={toggleMenu} />
        <Routes>
          <Route path="/" element={<OurModels />} />
          <Route path="/man" element={<Man />} />
          <Route path="/woman" element={<Woman />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/newsletter-sign" element={<Newsletter />} />
          <Route path="/newsletter" element={<NewsletterMain />} />
          <Route path="*" element={<Error />} />
          <Route path="/person" element={<Person />} />
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
