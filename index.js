const express = require('express');
const app = express();

const port = process.env.PORT || 8080;

app.get('/', (req, res) => {
  res.send('Hello from test, deployed to GCP Cloud Run!');
});

app.listen(port, () => {
  console.log('test listening on port ' + port);
});
