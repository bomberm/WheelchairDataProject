var express = require('express');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var exec = require('exec');
var child_process = require('child_process');
var fs = require('fs');
var crypto = require('crypto');
var path = require('path');
var PythonShell = require('python-shell');
var INI_JSON = null;
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
  if(test != INI_JSON){
          console.log("Initializing...", test);
          console.log("the following values should be different: ", test, " ", INI_JSON);
	  INI_JSON = test;
	  var dir = './bags/' + test + '/';
	  if (fs.existsSync(dir)){
	    testFile = dir+test+'.json';
	    var options = {
	      mode: 'text',
	      args: [testFile]
	    };

	    var pyshell = new PythonShell('./ROSHandling/launchFiles.py', options);

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
	}
  //else
  // Hadi, I need an error here to notifiy the user that the system cannot find the test file but I'm not sure how
});

// Added and works great!
app.get('/rosStartup',function(req,res){

    console.log("Startup...");
    var options = {
      mode: 'text',
    };

  var pyshell = new PythonShell('./ROSHandling/startup.py', options);

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

  var options = {
    mode: 'text',
    args: ["launch"]
  };
  PythonShell.run('./ROSHandling/shutdown.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
		console.log("Shutdown...");
    console.log('results: %j', results);
  });
});

function makeFile(name, launch, topics, test){
	testObject = {
    "name": testName,
    "ids": false,
    //"names": names.map(i=>i.trim()),
    "topics": topics.map(i=>i.trim()),
    "launch": launchFiles.map(i=>i.trim()).map(i=>i.split(' '))
  };

  if(test == true){
		testDir = "."
		}
  else{
		var testdir = './bags/'+testName;

		if (!fs.existsSync(testdir)){
				fs.mkdirSync(testdir);
		}
  }

  fs.writeFileSync((testdir+'/'+testName)+'.json', JSON.stringify(testObject, null, 2) , 'utf8');
}
	
app.get('/estimateBag', function(req,res){
		testName = req.query.name.replace(' ', '').toLowerCase();
		launchFiles = makeList(req.query.launch);
		topics = makeList(req.query.topics);

		makeFile(testName, launchFiles, topics, true);

		var options = {
				mode: 'text',
        args: ["./"+testName+".json"]
    	  }
  	var pyshell = new PythonShell('./ROSHandling/testBag.py', options);
		
		pyshell.on('message', function(message) {
				//do stuff
		});
});

app.get('/submitTest', function(req,res){
  const fs = require('fs')
  testName = req.query.name.replace(' ', '').toLowerCase();
  launchFiles = makeList(req.query.launch);
  topics = makeList(req.query.topics);
  //names = makeList(req.query.participants);

  makeFile(testName, launchFiles, topics, false); 
});

app.get('/testLaunch', function(req, res)
{

	console.log("Launching... ");	
  files = makeList(req.query.files).map(i=>i.trim()) //split on comma separation
  
  resp = {
		response: [],
    which: [], //if there is an error, which script failed?
    err: false //assume no error, will update if incorrect
    };
  
  var itemsComplete = 0;
  files.forEach(function(launchFile, index, array){
	  var options = {
	     mode: 'text',
       args: [launchFile]
     }

	var pyshell = new PythonShell('./ROSHandling/testLaunch.py', options);
	
  pyshell.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
		  console.log("Error: "+message);
    });
    
	// end the input stream and allow the process to exit
  pyshell.end(function (err,code,signal) {
    if (err){
      resp.err = true;
		  resp.which += launchFile;
      resp.err += err;
	  }

   console.log('The exit code was: ' + code);
   console.log('The exit signal was: ' + signal);
   console.log('finished');
   itemsComplete++;

	if(itemsComplete === array.length) {
	  respond(res, resp);
	  }

	});
    }, this);
});

function respond(res, resp){
  console.log(resp.err);
  res.send(resp);
}

app.get('/ros',function(req,res){
  name = req.query.name.replace(' ', '').toLowerCase();
  test = req.query.test.replace(' ', '').toLowerCase();
  const secret = test;
  const hash = crypto.createHmac('sha256', secret)
                   .update(name)
                   .digest('hex').substr(0, 6);
  var testdir = cwd + '/bags/' + test + '/';
  var namedir = testdir + hash + '/';

  if (!fs.existsSync(namedir)){
    fs.mkdirSync(namedir);
  }

  testFile = testdir+test+'.json';
  var options = {
    mode: 'text',
    args: [namedir, testFile]
  };
  PythonShell.run('./ROSHandling/startBag.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: %j', results);
  });

  res.send('command passed');
});

app.get('/kill',function(req,res){
	var options = {
		mode: 'text',
		args: 'bag',
	};

	PythonShell.run('./ROSHandling/shutdown.py', options, function (err, results) {
		if (err) throw err;
		// results is an array consisting of messages collected during execution
		console.log('results: %j', results);
  });

 res.send('command passed');
});


function makeList(input){
  return input.split(',');
}

function onExit(options, err){
		var options = {
				mode: 'text',
				args: 'launch',
		};

		PythonShell.run('./ROSHandling/shutdown.py', options, function (err, results) {
			if (err) throw err;
			// results is an array consisting of messages collected during execution
			console.log('results: %j', results);
  });

		options.args = 'core',
		PythonShell.run('./ROSHandling/shutdown.py', options, function (err, results) {
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
