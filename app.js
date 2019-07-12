const express = require("express");
const cors = require("cors");
const fs = require("fs");
const pdf = require("pdf-parse");
const multer = require("multer");

const upload = multer({});
const app = express();

app.use(cors());

app.get("/", (req, res) => {
  res.send("Hi");
});

app.post(
  "/fileUpload",
  multer({ dest: "./uploads" }).array("file-name", 1),
  (req, res) => {
    console.log(req.files);
    let dataBuffer = fs.readFileSync(req.files[0].path);
    pdf(dataBuffer).then(function(data) {
      // number of pages
      console.log(data.numpages);
      // number of rendered pages
      console.log(data.numrender);
      // PDF info
      console.log(data.info);
      // PDF metadata
      console.log(data.metadata);
      // PDF.js version
      // check https://mozilla.github.io/pdf.js/getting_started/
      console.log(data.version);
      // PDF text
      console.log(data.text);
    });
    res.send("Sucess");
  }
);

app.listen(4444, () => {
  console.log("Server started on http://localhost:4444");
});
