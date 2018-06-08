#!/usr/bin/python

from sys import argv
from time import sleep
import subprocess
import signal
import os


# Used in Create Test when 'test .launch' is pushed

if not len(argv) >= 2:
	raise IOError('Usage: '+argv[0]+' <.launch file>')

args = [i.split(' ') for i in argv[1:]]
command=["roslaunch"]
command.extend(args[0])

try:
	launch = subprocess.Popen(command, stdout =open(os.devnull, 'w') )
	sleep(1)
	launch.send_signal(signal.SIGINT)
	exit(0)

except Exception as error:
	raise
