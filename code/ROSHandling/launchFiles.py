#!/usr/bin/python

# Used in Run Test interface when 'initialize' button is pushed
import subprocess

scripts = [['wheelchair_description', 'wheelchair_bringup.launch'], ['wheelchair_description', 'wheelchair_merger.launch'], ['wheelchair_navigation', 'move_base_local.launch']]

store_pid = open("launch.pid", 'w')
store_log = []
error_log = []
for script in scripts:
	store_log.append(open(script[0]+'.log', 'w'))
	error_log.append(open(script[0]+'Error.log', 'w'))
	command=["roslaunch"]+script
	output = subprocess.Popen(command, stdout=store_log[-1], stderr=error_log[-1]) 
	store_pid.write(str(output.pid))
store_pid.close()
