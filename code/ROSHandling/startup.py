#/usr/bin/python
import subprocess
import os.path

#startup.py's core goal is to get roscore running on the robot and store the core pid. If roscore is already running, then the pid will be stored so that the test controller can shut it down if need be.  No input is required and any 'output' will be stored.

try:
	output = subprocess.check_output(["pgrep", "roscore"])
except Exception:
	output = False;

if not output: #check if roscore is already running
	output = subprocess.Popen('roscore') 
	output = output.pid
store_pid = open("core.pid", 'w')
store_pid.write(str(output))
store_pid.close()
