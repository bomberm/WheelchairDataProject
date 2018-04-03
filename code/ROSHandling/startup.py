#/usr/bin/python
import subprocess
import os.path

if os.path.isfile('core.pid'):
	exit(0)
corelog = open("core.log", 'w')
output = subprocess.Popen('roscore', stdout = corelog) 
store_pid = open("core.pid", 'w')
store_pid.write(str(output.pid))
store_pid.close()
