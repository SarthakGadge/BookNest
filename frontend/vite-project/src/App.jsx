import Navbar from "./components/Navbar";
import { Routes, Route } from "react-router-dom";
import GetStarted from "./components/GetStarted";
import AboutUs from "./components/AboutUs";
import LandingPage from "./components/LandingPage";
import ContactUs from "./components/ContactUs";

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/get-started" element={<GetStarted />} />
        <Route path="/about-us" element={<AboutUs />} />
        <Route path="/contact" element={<ContactUs />} />
      </Routes>
    </>
  );
}

export default App;
