import os
import signal
import sys

if len(sys.argv) == 2:
	pid = open(sys.argv[1]+".pid", 'r')
	for line in pid:
		os.kill(int(line), signal.SIGINT)
	pid.close()
	os.remove(sys.argv[1]+".pid")
