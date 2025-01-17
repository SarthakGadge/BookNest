import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <>
        <footer className="bg-gray-800 text-white py-4 text-center">
            <p className="text-sm">© 2025 BookNest. All rights reserved.</p>
            <nav className="mt-2">
            <Link to="/terms" className="mr-4 hover:text-gray-300">
            Terms
            </Link>
            <Link to="/privacy" className="hover:text-gray-300">
            Privacy
            </Link>
      </nav>
    </footer>
    </>
  )
}

export default Footer
