#/usr/bin/python

# Used in Run Test interface when 'start recording' is pushed.
import subprocess
import json
from sys import argv
from pathlib2 import Path

def get_pid(name):
	while 1:
		try:
    			return subprocess.check_output(["pidof",name])
		except:
			pass

if not len(argv) == 3:
	raise IOError('Usage: '+argv[0]+' <save_location> <test.json file>')

checkIfExists = Path(argv[2])
if checkIfExists.is_file:
	testFile = checkIfExists.open()
else:
	raise IOError('Usage: '+argv[2]+' must be a .json file.')

data = json.load(testFile)
topics = data['topics']

corelog = open("bag.log", 'w')
process = ['rosbag', 'record', '-o']
process.append(argv[1])
process = process+topics
print str(process)
output = subprocess.Popen(process, stdout=corelog)
storePid = open('bag.pid', 'w')
storePid.write(get_pid('record'))
storePid.close()
