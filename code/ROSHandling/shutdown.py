import os
import signal
import sys

if len(sys.argv) == 2:
	pid = open(sys.argv[1]+".pid", 'r')
	os.kill(int(pid), signal.SIGINT)
	pid_to_handle.close()
	os.remove(sys.argv[1]+".pid")
elif len(sys.argv) > 2:
	if not sys.argv[1].lower() == "launch":
		raise IOError('Usage: '+sys.argv[0]+' launch <test.json file>' 
	# Need to loop over all launch files and kill their pids
