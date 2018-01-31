import sys, os, shutil
sys.path.append("../")
from saveLocation import startSave
from readTestFile import readFile
from createFilesystem import createFilesystem
from testCreateFilesystem import cleanup

testFile = "../../Templates/TestFileTemplate.test"
IDFile = "../../Templates/IDFileTemplate.test"

f = readFile(testFile)
g = readFile(IDFile)
createFilesystem(f)
createFilesystem(g)

if not startSave('Joe Schmo', f):
	print "Could not locate secure name"
if not startSave(14, g):
	print "Could not locate ID"

cleanup('./Test Name/')
cleanup('./TestIDs/')
