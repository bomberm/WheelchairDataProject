#/usr/bin/python

# Used to test how large a bag file will be.

import os
import subprocess
from sys import argv
from time import sleep

if not len(argv) == 2:
		raise IOError('Usage: '+argv[0]+" <test.json file>")


output = subprocess.Popen(["python", "startBag.py", "./", argv[1]])

sleep(10)

subprocess.Popen(["python", "shutdown.py", "bag"])

files = os.listdir('.')

for name in files:
		if name.endswith(".bag.active"):
				bagfile = name

exit(os.path.getsize(bagfile))
