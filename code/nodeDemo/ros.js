var express = require('express');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var exec = require('exec');
var child_process = require('child_process');
var fs = require('fs');
var crypto = require('crypto');
var path = require('path')

var cwd = path.dirname(require.main.filename);
console.log(cwd);

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);

app.get('/',function(req,res){
  res.render('home');
});

app.get('/ros',function(req,res){
  //topics = req.query.topics;
  //console.log(topics);
  name = req.query.name.replace(' ', '').toLowerCase();
  const secret = 'chiron';
  const hash = crypto.createHmac('sha256', secret)
                   .update(name)
                   .digest('hex').substr(0, 6);
  topicString = "tf scan_multi pose_stamped";
  /*
  for(elem in topics){
    topicString += topics[elem];
    topicString += " ";
  }*/
  var dir = cwd + '/' + hash + '/';
  if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
  }
  child_process.exec('sh ' + "\"" +  cwd + '/startRecording.sh\" ' + dir + ' ' + topicString, function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
  res.send('command passed');
});

app.get('/kill',function(req,res){
  child_process.exec('kill `cat \"' + cwd + '/bag.pid\"`', function(err, out, code) {
    if (err instanceof Error)
      res.send('command returned error: ' + err)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
  res.send('command passed');
});


app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});
