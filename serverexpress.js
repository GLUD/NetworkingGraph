/* Ejemplo de como crear un servidor con expressjs */
var express = require('express');
var app = express();
app.use(express.static('dist'))
app.listen(8001, function() {
  console.log('Server Express Ready!');
});
