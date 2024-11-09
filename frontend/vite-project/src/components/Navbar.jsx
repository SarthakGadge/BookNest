import Logo1 from "../assets/logo.svg";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div className="flex items-center justify-between h-20 px-4 bg-black">
      <Link to="/">
        <img src={Logo1} alt="logo" className="h-10 w-20" />
      </Link>
      <div className="space-x-4">
        <Link
          to="/get-started"
          className="text-[#FEE715] px-4 py-2 rounded-xl shadow-md hover:bg-[#FEE715] hover:text-black transition duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg"
        >
          Get Started
        </Link>

        <Link
          to="/about-us"
          className="text-[#FEE715] px-4 py-2 rounded-xl shadow-md hover:bg-[#FEE715] hover:text-black transition duration-300 ease-in-out transform hover:scale-105 hover:shadow-lg"
        >
          About Us
        </Link>
      </div>
    </div>
  );
}
