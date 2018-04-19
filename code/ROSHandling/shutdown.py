import os
import signal
from sys import argv
from pathlib2 import Path




if len(argv) == 2:
	checkIfExists = Path(argv[1]+'.pid')
	if not checkIfExists.exists():
		exit(0)
	pid = open(argv[1]+".pid", 'r')
	for line in pid:
		os.kill(int(line), signal.SIGINT)
	pid.close()
	os.remove(argv[1]+".pid")
