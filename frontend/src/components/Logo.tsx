
import { Link } from "react-router-dom";

export const Logo = () => {
  return (
    <Link to="/" className="flex items-center">
      <span className="text-uw-white font-bold text-xl md:text-2xl">UW <span className="text-uw-gold">CourseMatch</span></span>
    </Link>
  );
};
