var express = require('express');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var exec = require('exec');
var child_process = require('child_process');
var fs = require('fs');
var crypto = require('crypto');
var path = require('path');
var PythonShell = require('python-shell');

/**
Copy the below snipper to add command line options to a python script
var options = {
  mode: 'text',
  args: ['my First Argument', 'My Second Argument', '--option=123']
};
**/

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

// Hadi, this is a function I added to initialize a test - Marie
app.get('/initialize',function(req,res){
  test = req.query.test.replace(' ', '').toLowerCase();
  var dir = cwd + '/' + test + '/';
  if (fs.existsSync(dir)){
    testFile = dir+test+'.json';
    var options = {
      mode: 'text',
      args: [testFile]
    };

    var pyshell = new PythonShell('../ROSHandling/launchFiles.py', options);

    pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      console.log(message);
    });
    // end the input stream and allow the process to exit
    pyshell.end(function (err,code,signal) {
      if (err) throw err;
      console.log('The exit code was: ' + code);
      console.log('The exit signal was: ' + signal);
      console.log('finished');
    });
  }
  //else
  // Hadi, I need an error here to notifiy the user that the system cannot find the test file but I'm not sure how
});

// Added and works great!
app.get('/rosStartup',function(req,res){

    var options = {
      mode: 'text',
    };

    /*
		PythonShell.run('../ROSHandling/startup.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: %j', results);
  });
  */

  var pyshell = new PythonShell('../ROSHandling/startup.py', options);

  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
  });
  // end the input stream and allow the process to exit
  pyshell.end(function (err,code,signal) {
    if (err) throw err;
    console.log('The exit code was: ' + code);
    console.log('The exit signal was: ' + signal);
    console.log('finished');
  });
});


app.get('/shutdown', function(req, res){
  /**
  child_process.exec('python ../ROSHandling/shutdown.py launch', function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
  */
  var options = {
    mode: 'text',
    args: ["launch"]
  };
  PythonShell.run('../ROSHandling/shutdown.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: %j', results);
  });
});

app.get('/ros',function(req,res){
  name = req.query.name.replace(' ', '').toLowerCase();
  test = req.query.test.replace(' ', '').toLowerCase();
  const secret = test;
  const hash = crypto.createHmac('sha256', secret)
                   .update(name)
                   .digest('hex').substr(0, 6);
  var testdir = cwd + '/' + test + '/';
  var namedir = testdir + hash + '/';

  if (!fs.existsSync(namedir)){
    fs.mkdirSync(namedir);
  }

  testFile = testdir+test+'.json';
  var options = {
    mode: 'text',
    args: [namedir, testFile]
  };
  PythonShell.run('../ROSHandling/startBag.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: %j', results);
  });

    /**
    child_process.exec('python ../ROSHandling/startUp.py ' + namedir + ' ' + testFile , function(err, out, code) {
    if (err instanceof Error)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
  });
  **/

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

  //child_process.exec('python '+ cwd + '/../ROSHandling/shutdown.py core', function(err, out, code) {
   // if (err instanceof Error)
    //  res.send('command returned error: ' + err)
   ///  throw err;
   // process.stderr.write(err);
   //  process.stdout.write(out);
   // process.exit(code);
  //});
 res.send('command passed');
});


function onExit(options, err){
		var options = {
				mode: 'text',
				args: 'launch',
		};

		PythonShell.run('../ROSHandling/shutdown.py', options, function (err, results) {
			if (err) throw err;
			// results is an array consisting of messages collected during execution
			console.log('results: %j', results);
  });

		options.args = 'core',
		PythonShell.run('../ROSHandling/shutdown.py', options, function (err, results) {
			if (err) throw err;
			// results is an array consisting of messages collected during execution
			console.log('results: %j', results);
  });

    if (err) console.log(err.stack);
    process.exit();
}

process.on('exit', onExit.bind(null, {exit: true}));

process.on('SIGINT', onExit.bind(null, {exit: true}));

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
