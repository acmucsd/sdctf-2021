const spawn = require('child_process').spawn;

const express = require('express');
const PORT = process.env.PORT || 8080;
const app = express();

const BUFFER_SIZE = 8;

app.get('/prime', (req, res) => {
  if(!req.query.n) {
    res.status(400).send('Missing required parameter n');
    return;
  }

  if(req.query.n.length > BUFFER_SIZE) {
    res.status(400).send('Requested n too large!');
    return;
  }

  let output = '';
  const proc = spawn(__dirname + '/primegen');
  proc.stdout.on('data', data => output += data.toString());
  proc.on('exit', () => res.send(output));

  // call our super-efficient native prime generator!
  proc.stdin.write(`${req.query.n}\n`);
})

app.use('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.use('*', (req, res) => {
  res.status(404).send('Not Found');
});

app.listen(PORT, () => {
  console.log(`prime generator listening at http://localhost:${PORT}`)
})
