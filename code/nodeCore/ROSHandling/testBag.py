#/usr/bin/python

# Used to test how large a bag file will be.

import os
import subprocess
from sys import argv
from sys import path
from time import sleep

path.append("./ROSHandling/")

if not len(argv) == 2:
		raise IOError('Usage: '+argv[0]+" <test.json file>")


output = subprocess.Popen(["python", "./ROSHandling/startBag.py", "./", argv[1]], stdout=open(os.devnull, 'w'))

sleep(10)

subprocess.Popen(["python", "./ROSHandling/shutdown.py", "bag"])

sleep(1)

files = os.listdir('.')

for name in files:
		if ".bag" in name:
				bagfile = name

print os.path.getsize(bagfile)
os.remove(bagfile)
sleep(1)
