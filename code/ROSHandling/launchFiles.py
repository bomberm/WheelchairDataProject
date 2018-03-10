import subprocess

scripts = ['wheelchair_description wheelchair_bringup.launch', 'wheelchair_description wheelchair_merger.launch', 'wheelchair_navigation move_base_local.launch']

store_pid = open("launch.pid", 'w')
store_log = []
for script in scripts:
	store_log.append(open(script+'.log', 'w'))
	output = subprocess.Popen('roslaunch '+script, stdout=store_log[-1]) 
	store_pid.write(str(output.pid))
store_pid.close()
