import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link> |
      <Link to="/jobs"> Jobs</Link> |
      <Link to="/employer"> Employer</Link> |
      <Link to="/candidate"> Candidate</Link> |
      <Link to="/login"> Login</Link> |
      <Link to="/register"> Register</Link>
    </nav>
  );
}

export default Navbar;