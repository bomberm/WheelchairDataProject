#!/usr/bin/python
import startup, launchFiles, startBag
import sys

startup
launchFiles
os.system("startBag "+ sys.argv[1:])
