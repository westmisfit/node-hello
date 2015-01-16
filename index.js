var express = require('express');
var app = express();
var log4js = require('log4js');
log4js.configure('log4js.json', { cwd: __dirname });
var logger = log4js.getLogger('node-hello');

var EOL = require('os').EOL;

app.use(function (req, res, next) {
  logger.debug(req.originalUrl);
  next();
});

app.get('/', function (req, res) {
  res.send(['Hello World!','Date 2015-01-16 0001',''].join(EOL));
});

app.get('/ping', function (req, res) {
  res.send(['pong',''].join(EOL));
});

var port = process.env.PORT || 3000;

var server = app.listen(port, function () {

  var host = server.address().address;
  var port = server.address().port;

  logger.debug('Example app listening at http://%s:%s', host, port);

});