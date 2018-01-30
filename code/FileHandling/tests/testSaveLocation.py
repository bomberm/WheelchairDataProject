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

startSave('Joe Schmo', f)
startSave(14, g)

cleanup('./Test Name/')
cleanup('./TestIDs/')
