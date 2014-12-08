var express = require('express')
var app = express()

var EOL = require('os').EOL;

app.use(function (req, res, next) {
  console.log(req.originalUrl);
  next();
})

app.get('/', function (req, res) {
  res.send(['Hello World!',''].join(EOL));
})

app.get('/ping', function (req, res) {
  res.send(['pong',''].join(EOL));
})

var port = process.env.PORT || 3000

var server = app.listen(port, function () {

  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)

})