/* Ejemplo de como crear un servidor con expressjs */
var heroku_port   = process.env.PORT;
console.log('heroku_port', heroku_port);
var express = require('express');
var app = express();
app.use(express.static('dist'))
app.listen(heroku_port, function() {
  console.log('Server Express Ready!');
});
