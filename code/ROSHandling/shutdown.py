import os
import signal
import sys

if len(sys.argv) > 1:
	pid_to_handle = open(sys.argv[1]+".pid", 'r')
	for line in pid_to_handle:
		os.kill(int(line), signal.SIGINT)
	pid_to_handle.close()
	os.remove(sys.argv[1]+".pid")

