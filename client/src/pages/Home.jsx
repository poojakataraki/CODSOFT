import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h1>Job Board Portal</h1>

      <p>
        Connecting Employers and Job Seekers.
      </p>

      <h2>Featured Jobs</h2>

      <ul>
        <li>Software Engineer</li>
        <li>Frontend Developer</li>
        <li>AI Engineer</li>
      </ul>

      <Link to="/jobs">
        <button>Browse Jobs</button>
      </Link>
    </div>
  );
}

export default Home;