#/usr/bin/python
import subprocess

corelog = open("core.log", 'w')
output = subprocess.Popen('roscore', stdout = corelog) 
store_pid = open("core.pid", 'w')
store_pid.write(str(output.pid))
store_pid.close()
