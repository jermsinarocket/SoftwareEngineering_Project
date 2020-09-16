const fs = require('fs');
const express = require('express');
const path = require('path');
const app = express();
const conf = require('config');
const port = conf.get('port');
const pluginOptimizer = require("./public/pluginOptimizer");

pluginOptimizer.generateBuildFiles();
// Define the port to run on
app.set('port', port); //

//app.use('/nodejs-web-plugin',express.static(path.join(__dirname,'')));
app.use(express.static(path.join(__dirname, '/public')));
app.get('/', function (request, response) {
  response.sendFile(__dirname + '/index.html');
});

//Listen for requests
var server = app.listen(app.get('port'), function () {
  var port = server.address().port;
  pluginOptimizer.updateDataAsPerEnv();
  console.log('Open localhost using port ' + port); //
});
