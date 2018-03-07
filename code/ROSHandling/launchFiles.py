import subprocess

scripts = ['wheelchair_description wheelchair_bringup.launch', 'wheelchair_description wheelchair_merger.launch', 'wheelchair_navigation move_base_local.launch']

store_pid = open("launch.pid", 'w')
for script in scripts:
	output = subprocess.Popen('roslaunch '+script, 
	store_pid.write(str(
