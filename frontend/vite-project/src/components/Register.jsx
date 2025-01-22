import { useState } from "react";

const Register = () => {

  const [success, setSuccess] = useState(null);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [username, setUsername] = useState("");
  const [error, setError] = useState(null);
  // const [showPassword, setShowPassword] = useState(false);

  // const togglePasswordVisibility = () => {
  //   setShowPassword((prevState) => !prevState); // Toggle the visibility state
  // };

  const handleregister = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    const userData = {
      email: email,
      password: password,
      username: username
    };

    if(password !== confirmPassword){
      setError("Passwords do not match");
      return;
    }

    try{
      const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.msg);
      }

      const data = await response.json();
      setSuccess(data.msg);
    }

    catch (error) {
      setError(error.message || error.msg || "An unexpected error occurred");
    }

  }

  return (
      <>
        <main className="bg-gradient-to-br from-gray-900 via-black to-gray-800 text-[#FEE715] flex justify-center items-center min-h-screen px-4 sm:px-8 lg:px-0 py-20">
          <section className="bg-black/75 p-6 sm:p-8 md:p-10 rounded-lg shadow-2xl border-2 border-[#FEE715] max-w-md sm:max-w-lg w-full">
            <h1 className="text-2xl sm:text-3xl md:text-4xl font-bold text-center mb-6 md:mb-8">
              Welcome Back
            </h1>
            <form className="flex flex-col space-y-4 sm:space-y-6">
              <div className="flex flex-col">
                <label htmlFor="email" className="text-sm sm:text-base font-medium mb-1 sm:mb-2">
                  Email
                </label>
                <input
                  id="email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter your email"
                  className="w-full p-2 sm:p-3 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
                />
              </div>
              <div className="flex flex-col">
                <label htmlFor="username" className="text-sm sm:text-base font-medium mb-1 sm:mb-2">
                  Username
                </label>
                <input
                  id="username"
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="Enter your username"
                  className="w-full p-2 sm:p-3 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
                />
              </div>
              <div className="flex flex-col">
                <label htmlFor="password" className="text-sm sm:text-base font-medium mb-1 sm:mb-2">
                  Password
                </label>
                <input
                  id="password"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter your password"
                  className="w-full p-2 sm:p-3 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
                />
              </div>
              <div className="flex flex-col">
                <label htmlFor="confirm_password" className="text-sm sm:text-base font-medium mb-1 sm:mb-2">
                  Confirm Password
                </label>
                <input
                  id="confirm_password"
                  type="password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  placeholder="Re-enter your password"
                  className="w-full p-2 sm:p-3 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
                />
              </div>
              {error && (
              <p className="text-red-500 text-sm text-center">{error}</p>
              )}
              {success && (
                <p className="text-green-500 text-sm text-center">{success}</p>
              )}
              <button
                type="submit"
                onClick={handleregister}
                className="w-full py-2 sm:py-3 bg-[#FEE715] text-black font-bold rounded-lg hover:bg-yellow-400 transition duration-200"
              >
                Register
              </button>
              <p className="text-center text-xs sm:text-sm text-gray-400">
                Already have an account?{" "}
                <a
                  href="/get-started"
                  className="text-[#FEE715] hover:text-yellow-400 underline"
                >
                  Sign In
                </a>
              </p>
            </form>
          </section>
        </main>
      </>
    );
  };
  
  export default Register;
  