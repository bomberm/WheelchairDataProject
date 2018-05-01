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
if not 'launch' in data.keys():
	exit(0)
scripts = data['launch']

store_pid = open("launch.pid", 'w')
for script in scripts:
	command=["roslaunch"]+script
	output = subprocess.Popen(command) 
	store_pid.write(str(output.pid))
store_pid.close()
