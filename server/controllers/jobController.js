const Job = require("../models/Job");

const createJob = async (req, res) => {
  try {

    const job = new Job(req.body);

    await job.save();

    res.status(201).json(job);

  } catch (error) {

    res.status(500).json({
      message: error.message
    });

  }
};

const getJobs = async (req, res) => {
  try {

    const jobs = await Job.find();

    res.json(jobs);

  } catch (error) {

    res.status(500).json({
      message: error.message
    });

  }
};

const getJobById = async (req, res) => {
  try {

    const job = await Job.findById(
      req.params.id
    );

    if (!job) {
      return res.status(404).json({
        message: "Job not found"
      });
    }

    res.json(job);

  } catch (error) {

    res.status(500).json({
      message: error.message
    });

  }
};

module.exports = {
  createJob,
  getJobs,
  getJobById
};