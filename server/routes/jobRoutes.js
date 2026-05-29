const express = require("express");
const router = express.Router();

const auth =
require("../middleware/authMiddleware");

const {
  createJob,
  getJobs,
  getJobById
} = require(
  "../controllers/jobController"
);

router.post(
  "/",
  auth,
  createJob
);

router.get(
  "/",
  getJobs
);

router.get(
  "/:id",
  getJobById
);

module.exports = router;