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

app.get('/configure',function(req,res){
  res.render('configure');
});

app.get('/launch',function(req, res){
  launchPath = req.query.launch;

  //code for general case overwritten and hardcoded below
  /*
  child_process.exec('sh ' + "\"" +  cwd + '/startRecording.sh\" ' + dir + ' ' + topicString, function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
  */

  child_process.exec('python ../ROSHandling/launchFiles.py', function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });

});

// Hadi, this is a function I added to initialize a test - Marie
app.get('/initialize',function(req,res){
  test = req.query.test.replace(' ', '');
  var dir = cwd + '/' + test + '/';
  if (fs.existsSync(dir)){
    testFile = dir+test+'.json';
    child_process.exec('python ../ROSHandling/launchFiles.py '+testFile, function(err, out, code) {
      if (err instanceof Error)
        throw err;
      process.stderr.write(err);
      process.stdout.write(out);
      process.exit(code);
    }); 
  };
  //else
  // Hadi, I need an error here to notifiy the user that the system cannot find the test file but I'm not sure how
});
 
// Added and works great!
app.get('/rosStartup',function(req,res){
  child_process.exec('python ../ROSHandling/startup.py', function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
});

app.get('/shutdown', function(req, res){
  child_process.exec('python ../ROSHandling/shutdown.py launch', function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
});

app.get('/ros',function(req,res){
  //topics = req.query.topics;
  //console.log(topics);
  name = req.query.name.replace(' ', '').toLowerCase();
  const secret = 'chiron';
  const hash = crypto.createHmac('sha256', secret)
                   .update(name)
                   .digest('hex').substr(0, 6);
  /*
  for(elem in topics){
    topicString += topics[elem];
    topicString += " ";
  }*/
  var dir = cwd + '/' + hash + '/';
  if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
  }
  child_process.exec('python ' + "\"" +  cwd + '/../ROSHandling/barebones.py" ' + dir + ' ' + '../Templates/Chiron.json', function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
  res.send('command passed');
});

app.get('/kill',function(req,res){
  child_process.exec('python '+ cwd + '/../ROSHandling/shutdown.py bag', function(err, out, code) {
    if (err instanceof Error)
      res.send('command returned error: ' + err)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });

  child_process.exec('python '+ cwd + '/../ROSHandling/shutdown.py core', function(err, out, code) {
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
