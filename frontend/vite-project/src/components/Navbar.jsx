import Logo1 from "../assets/logo.svg";
import { NavLink } from "react-router-dom";
import { useState, useEffect } from "react";

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <nav
      className={`p-4 text-black dark:text-white dark:bg-black flex justify-between items-center sticky top-0 z-50 transition-all duration-300 ease-in-out ${
        scrolled ? "shadow-lg bg-[#A35C7A]" : ""
      }`}
    >
      {/* Logo */}
      <NavLink to="/">
        <img src={Logo1} alt="logo" className="h-10 w-20" />
      </NavLink>

      {/* Hamburger Menu Button */}
      <button
        className="block md:hidden focus:outline-none"
        onClick={() => setMenuOpen(!menuOpen)}
      >
        <span className="block w-6 h-1 bg-[#FEE715] mb-1.5"></span>
        <span className="block w-6 h-1 bg-[#FEE715] mb-1.5"></span>
        <span className="block w-6 h-1 bg-[#FEE715]"></span>
      </button>

      {/* Navbar Links */}
      <div
        className={`${
          menuOpen ? "block" : "hidden"
        } absolute top-full left-0 w-full bg-[#A35C7A] md:bg-transparent md:static md:flex md:space-x-4 md:items-center md:justify-end`}
      >
        <NavLink
          to="/get-started"
          className={({ isActive }) =>
            `block px-4 py-2 rounded-xl md:inline shadow-md transition duration-300 ease-in-out transform hover:scale-105 ${
              isActive
                ? "bg-[#FEE715] text-black"
                : "text-[#FEE715] hover:bg-[#FEE715] hover:text-black"
            }`
          }
        >
          Get Started
        </NavLink>

        <NavLink
          to="/about-us"
          className={({ isActive }) =>
            `block px-4 py-2 rounded-xl md:inline shadow-md transition duration-300 ease-in-out transform hover:scale-105 ${
              isActive
                ? "bg-[#FEE715] text-black"
                : "text-[#FEE715] hover:bg-[#FEE715] hover:text-black"
            }`
          }
        >
          About Us
        </NavLink>
      </div>
    </nav>
  );
}
