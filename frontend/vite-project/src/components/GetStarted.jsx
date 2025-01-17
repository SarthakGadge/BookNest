const GetStarted = () => {
  return (
    <>
      
      <main className="bg-gradient-to-br from-gray-900 via-black to-gray-800 text-[#FEE715] flex justify-center items-center h-screen">
  <section className="bg-black/75 p-10 rounded-lg shadow-2xl border-2 border-[#FEE715] max-w-sm w-full">
    <h1 className="text-4xl font-bold text-center mb-8">Welcome Back</h1>
    <form className="flex flex-col space-y-6">
      <div className="flex flex-col">
        <label htmlFor="email" className="text-sm font-medium mb-2">
          Email
        </label>
        <input
          id="email"
          type="email"
          placeholder="Enter your email"
          className="w-full p-3 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
        />
      </div>
      <div className="flex flex-col">
        <label htmlFor="password" className="text-sm font-medium mb-2">
          Password
        </label>
        <input
          id="password"
          type="password"
          placeholder="Enter your password"
          className="w-full p-3 rounded-lg bg-gray-800 text-white placeholder-gray-400 focus:ring-2 focus:ring-[#FEE715] focus:outline-none"
        />
      </div>
      <button
        type="submit"
        className="w-full py-3 bg-[#FEE715] text-black font-bold rounded-lg hover:bg-yellow-400 transition duration-200"
      >
        Log In
      </button>
      <p className="text-center text-sm text-gray-400">
        Don&apos;t have an account?{" "}
        <a
          href="#"
          className="text-[#FEE715] hover:text-yellow-400 underline"
        >
          Sign Up
        </a>
      </p>
    </form>
  </section>
</main>

      
    </>
  );
};

export default GetStarted;
