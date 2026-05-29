const express = require("express");
const router = express.Router();

const upload =
require("../middleware/upload");

const auth =
require("../middleware/authMiddleware");

const {
  applyJob,
  getApplications
} = require(
  "../controllers/applicationController"
);

router.post(
  "/",
  auth,
  upload.single("resume"),
  applyJob
);

router.get(
  "/my",
  auth,
  getApplications
);

module.exports = router;