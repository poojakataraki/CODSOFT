import { useState } from "react";
import api from "../services/api";

function EmployerDashboard() {

  const [job, setJob] = useState({
    title: "",
    company: "",
    location: "",
    salary: "",
    description: ""
  });

  const createJob = async () => {

    try {

      const token =
        localStorage.getItem("token");

      await api.post(
        "/jobs",
        job,
        {
          headers: {
            Authorization: token
          }
        }
      );

      alert("Job Posted Successfully");

    } catch (error) {

      console.log(error);

      alert("Error Posting Job");

    }
  };

  return (
    <div>

      <h1>Employer Dashboard</h1>

      <input
        placeholder="Job Title"
        onChange={(e)=>
        setJob({
          ...job,
          title:e.target.value
        })}
      />

      <input
        placeholder="Company"
        onChange={(e)=>
        setJob({
          ...job,
          company:e.target.value
        })}
      />

      <input
        placeholder="Location"
        onChange={(e)=>
        setJob({
          ...job,
          location:e.target.value
        })}
      />

      <input
        placeholder="Salary"
        onChange={(e)=>
        setJob({
          ...job,
          salary:e.target.value
        })}
      />

      <textarea
        placeholder="Description"
        onChange={(e)=>
        setJob({
          ...job,
          description:e.target.value
        })}
      />

      <br/>

      <button onClick={createJob}>
        Create Job
      </button>

    </div>
  );
}

export default EmployerDashboard;