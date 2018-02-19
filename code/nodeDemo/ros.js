var express = require('express');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var exec = require('exec');
var child_process = require('child_process');

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 3000);

app.get('/',function(req,res){
  res.render('home');
});

app.get('/ros',function(req,res){
  child_process.exec('sh /home/chiron/startRecording.sh /home/chiron/WheelchairDataProject/code/Connection/test/ tf', function(err, out, code) {
    if (err instanceof Error)
      res.send('command returned error: ' + err)
      throw err;
    process.stderr.write(err);
    process.stdout.write(out);
    process.exit(code);
    res.send('command executed. debug response: ' + out);
  });
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
