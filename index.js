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
  setTimeout(function(){
    res.send(['Hello World!',''].join(EOL));
  }, 100)
});

var _request_count = 1;

app.get('/wait/:time', function (req, res) {
  var request_no = "[" + (_request_count++) + "]";
  logger.debug(request_no + " wait for " + req.params.time + "ms")
  setTimeout(function(){
    logger.debug(request_no + " delayed " + req.params.time + "ms")
    res.send(['Hello World!','Date 2015-01-20',''].join(EOL));
  }, req.params.time);
});

app.get('/ping', function (req, res) {
  res.send(['pong',''].join(EOL));
});

setTimeout(function init() {
  var port = process.env.PORT || 3000;

  var server = app.listen(port, function () {

    var host = server.address().address;
    var port = server.address().port;

    logger.debug('Example app listening at http://%s:%s', host, port);

  });

  process.on('SIGTERM', function() {
    server.close(function(){
      console.log('the server is terminated');
      process.exit(0);
    });
  });
}, 3000);
