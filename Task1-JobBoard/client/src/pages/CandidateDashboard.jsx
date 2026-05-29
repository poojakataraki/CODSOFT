import { useEffect, useState }
from "react";

import api
from "../services/api";

function CandidateDashboard() {

  const [applications,
  setApplications]
  = useState([]);

  useEffect(() => {

    fetchApplications();

  }, []);

  const fetchApplications =
  async () => {

    try {

      const token =
      localStorage.getItem(
      "token"
      );

      const res =
      await api.get(
      "/applications/my",
      {
        headers:{
          Authorization:
          token
        }
      });

      setApplications(
      res.data
      );

    } catch(error) {

      console.log(error);

    }
  };

  return (
    <div>

      <h1>
      My Applications
      </h1>

      {applications.map(app => (

        <div
        key={app._id}
        style={{
          border:"1px solid gray",
          padding:"10px",
          margin:"10px"
        }}
        >

          <p>
            Job ID:
            {app.jobId}
          </p>

          <p>
            Resume:
            {app.resume}
          </p>

        </div>

      ))}

    </div>
  );
}

export default CandidateDashboard;