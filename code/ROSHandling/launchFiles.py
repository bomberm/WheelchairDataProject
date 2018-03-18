#!/usr/bin/python

# Used in Run Test interface when 'initialize' button is pushed
import subprocess #run the launch routines
import json #json handling
from sys import argv #access args
from pathlib2 import Path

if not len(argv) == 2:
	raise IOError('Usage: '+argv[0]+' <test.json file>')

checkIfExists = Path(argv[1])
if checkIfExists.is_file:
	testFile = checkIfExists.open()
else:
	raise IOError('Usage: '+argv[1]+'must be a .json file')	

data = json.load(testFile)
scripts = data['launch']

store_pid = open("launch.pid", 'w')
store_log = []
error_log = []
for script in scripts:
	print script
	store_log.append(open(script[0]+'.log', 'w'))
	error_log.append(open(script[0]+'Error.log', 'w'))
	command=["roslaunch"]+script
	output = subprocess.Popen(command, stdout=store_log[-1], stderr=error_log[-1]) 
	store_pid.write(str(output.pid))
store_pid.close()
