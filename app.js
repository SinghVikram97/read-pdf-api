const express = require("express");
const cors = require("cors");
const fs = require("fs");
const pdf = require("pdf-parse");
const multer = require("multer");

const { PythonShell } = require("python-shell");

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
      // PDF text

      let options = {
        args: [data.text]
      };

      PythonShell.run("predict.py", options, (err, result) => {
        if (err) {
          throw err;
        }
        console.log(result);
        res.json(result);
      });
    });
  }
);

app.listen(4444, () => {
  console.log("Server started on http://localhost:4444");
});
