const Application = require("../models/Application");

const applyJob = async (req, res) => {
  try {

    const application = new Application({
      userId: req.user.id,
      jobId: req.body.jobId,
      resume: req.file
        ? req.file.filename
        : ""
    });

    await application.save();

    res.status(201).json(application);

  } catch (error) {

    res.status(500).json({
      message: error.message
    });

  }
};

const getApplications = async (req, res) => {
  try {

    const applications =
      await Application.find({
        userId: req.user.id
      });

    res.json(applications);

  } catch (error) {

    res.status(500).json({
      message: error.message
    });

  }
};

module.exports = {
  applyJob,
  getApplications
};