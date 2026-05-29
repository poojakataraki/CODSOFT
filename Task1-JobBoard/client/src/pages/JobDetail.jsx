import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

function JobDetail() {

  const { id } = useParams();

  const [job, setJob] = useState(null);

  useEffect(() => {

    fetchJob();

  }, []);

  const fetchJob = async () => {

    try {

      const res =
      await api.get(
        `/jobs/${id}`
      );

      setJob(res.data);

    } catch(error) {

      console.log(error);

    }
  };

  if (!job) {
    return <h2>Loading...</h2>;
  }

  return (
    <div>

      <h1>{job.title}</h1>

      <p>
        <strong>Company:</strong>
        {job.company}
      </p>

      <p>
        <strong>Location:</strong>
        {job.location}
      </p>

      <p>
        <strong>Salary:</strong>
        {job.salary}
      </p>

      <p>
        <strong>Description:</strong>
        {job.description}
      </p>

    </div>
  );
}

export default JobDetail;