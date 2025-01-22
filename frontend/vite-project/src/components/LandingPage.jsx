import { useNavigate } from "react-router-dom";
import Button from "../components/Button";
import { BookOpen, Users, Star } from "lucide-react";

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <main className="flex-1 bg-gradient-to-br from-gray-900 via-black to-gray-800">
        {/* Hero Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col items-center space-y-6 text-center">
              <div className="space-y-4">
                <h1 className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl lg:text-6xl text-[#FEE715]/80">
                  Welcome to BookNest
                </h1>
                <p className="mx-auto max-w-[700px] text-[#FEE715]/80 text-sm sm:text-base md:text-lg">
                  Your personal library in the cloud. Organize, discover, and
                  enjoy your books like never before.
                </p>
              </div>
              <div className="space-x-4">
                <Button
                  variant="primary"
                  onClick={() => navigate("/get-started")}
                >
                  Get Started
                </Button>
              </div>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section
          id="features"
          className="w-full py-12 md:py-24 lg:py-32 bg-[#FEE715] text-[#101820]"
        >
          <div className="container px-4 sm:px-6 lg:px-8">
            <h2 className="text-2xl font-bold tracking-tight sm:text-3xl md:text-4xl text-center mb-12">
              Features
            </h2>
            <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
              <div className="flex flex-col items-center space-y-4 text-center">
                <BookOpen className="h-10 w-10 sm:h-12 sm:w-12" />
                <h3 className="text-lg sm:text-xl font-bold">
                  Virtual Bookshelf
                </h3>
                <p className="text-sm sm:text-base text-[#101820]/80">
                  Organize your books digitally with ease.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <Users className="h-10 w-10 sm:h-12 sm:w-12" />
                <h3 className="text-lg sm:text-xl font-bold">Book Clubs</h3>
                <p className="text-sm sm:text-base text-[#101820]/80">
                  Connect with other readers and share your thoughts.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <Star className="h-10 w-10 sm:h-12 sm:w-12" />
                <h3 className="text-lg sm:text-xl font-bold">
                  Personalized Recommendations
                </h3>
                <p className="text-sm sm:text-base text-[#101820]/80">
                  Discover new books based on your reading history.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section id="contact" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 sm:px-6 lg:px-8">
            <h2 className="text-2xl font-bold tracking-tight sm:text-3xl md:text-4xl text-center mb-12 text-[#FEE715]">
              Contact Us
            </h2>
            <div className="mx-auto max-w-[600px]">
              <form className="space-y-4">
                <input
                  placeholder="Your Name"
                  className="bg-[#101820] text-[#FEE715] placeholder-[#FEE715]/50 border border-[#FEE715] p-3 rounded-md w-full"
                />
                <input
                  placeholder="Your Email"
                  type="email"
                  className="bg-[#101820] text-[#FEE715] placeholder-[#FEE715]/50 border border-[#FEE715] p-3 rounded-md w-full"
                />
                <textarea
                  className="min-h-[100px] w-full rounded-md border border-[#FEE715] bg-[#101820] p-3 text-sm text-[#FEE715] placeholder-[#FEE715]/50 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
                  placeholder="Your Message"
                ></textarea>
                <Button variant="primary">Send Message</Button>
              </form>
            </div>
          </div>
        </section>
      </main>
    </>
  );
};

export default LandingPage;
