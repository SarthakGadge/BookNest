import PropTypes from "prop-types";
import classNames from "classnames";

const Button = ({ variant = "primary", size = "md", children, ...props }) => {
  const baseStyles =
    "rounded-xl px-4 py-2 transition duration-300 ease-in-out transform";

  const variantStyles = {
    primary:
      "bg-[#FEE715] text-[black] hover:bg-white hover:text-black shadow-md",
    secondary:
      "bg-black text-[#FEE715] hover:bg-white hover:text-black shadow-md",
  };

  const sizeStyles = {
    sm: "text-sm",
    md: "text-base",
    lg: "text-lg",
  };

  return (
    <button
      className={classNames(
        baseStyles,
        variantStyles[variant],
        sizeStyles[size]
      )}
      {...props}
    >
      {children}
    </button>
  );
};

Button.propTypes = {
  variant: PropTypes.oneOf(["primary", "secondary"]),
  size: PropTypes.oneOf(["sm", "md", "lg"]),
  children: PropTypes.node.isRequired,
};

export default Button;
