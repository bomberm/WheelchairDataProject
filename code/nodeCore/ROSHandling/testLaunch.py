#!/usr/bin/python

from launchFiles import launch
from sys import argv
from time import sleep
import subprocess
import signal


# Used in Create Test when 'test .launch' is pushed

if not len(argv) >= 2:
	raise IOError('Usage: '+argv[0]+' <.launch file>')

command=["roslaunch"]+argv[1:]
try:
	launch = subprocess.Popen(command)
	sleep(.5)
	launch.send_signal(signal.SIGINT)
	exit(0)

except Exception as error:
	print "Cause error"
	raise