import { useNavigate } from "react-router-dom";
import Button from "../components/Button";
import { BookOpen, Users, Star } from "lucide-react";

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <main className="flex-1 bg-black">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none text-[#FEE715]/80">
                  Welcome to BookNest
                </h1>
                <p className="mx-auto max-w-[700px] text-[#FEE715]/80 md:text-xl">
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
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12">
              Features
            </h2>
            <div className="grid gap-10 sm:grid-cols-2 md:grid-cols-3">
              <div className="flex flex-col items-center space-y-3 text-center">
                <BookOpen className="h-12 w-12" />
                <h3 className="text-xl font-bold">Virtual Bookshelf</h3>
                <p className="text-[#101820]/80">
                  Organize your books digitally with ease.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-3 text-center">
                <Users className="h-12 w-12" />
                <h3 className="text-xl font-bold">Book Clubs</h3>
                <p className="text-[#101820]/80">
                  Connect with other readers and share your thoughts.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-3 text-center">
                <Star className="h-12 w-12" />
                <h3 className="text-xl font-bold">
                  Personalized Recommendations
                </h3>
                <p className="text-[#101820]/80">
                  Discover new books based on your reading history.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section id="contact" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12">
              Contact Us
            </h2>
            <div className="mx-auto max-w-[600px]">
              <form className="space-y-4">
                <input
                  placeholder="Your Name"
                  className="bg-[#101820] text-[#FEE715] placeholder-[#FEE715]/50 border-[#FEE715] p-2 rounded-md w-full"
                />
                <input
                  placeholder="Your Email"
                  type="email"
                  className="bg-[#101820] text-[#FEE715] placeholder-[#FEE715]/50 border-[#FEE715] p-2 rounded-md w-full"
                />
                <textarea
                  className="min-h-[100px] w-full rounded-md border border-[#FEE715] bg-[#101820] px-3 py-2 text-sm text-[#FEE715] placeholder-[#FEE715]/50 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#FEE715] focus-visible:ring-offset-2"
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
