#/usr/bin/python

# Used to test how large a bag file will be.

import os
import subprocess
from sys import argv
from time import sleep

if not len(argv) == 2:
		raise IOError('Usage: '+argv[0]+" <test.json file>")


output = subprocess.Popen(["python", "startBag.py", "./", argv[1]], stdout=open(os.devnull, 'w'))

sleep(10)

subprocess.Popen(["python", "shutdown.py", "bag"])

sleep(1)

files = os.listdir('.')

for name in files:
		if ".bag" in name:
				bagfile = name

print os.path.getsize(bagfile)
os.remove(bagfile)
