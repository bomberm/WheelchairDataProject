#/usr/bin/python

import subprocess
import sys

def get_pid(name):
    return subprocess.check_output(["pidof",name])

if len(sys.argv) < 3:
	print "Usage: "+sys.argv[0]+" <location> <topic(s)>"
	exit(-1)	
corelog = open("bag.log", 'w')
process = ['rosbag', 'record', '-o']
process = process + sys.argv[1:]
output = subprocess.Popen(process, stdout=corelog)
storePid = open('bag.pid', 'w')
storePid.write(get_pid('record'))
storePid.close()
