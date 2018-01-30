import sys, os, shutil
sys.path.append("../")
import createFilesystem as create
import readTestFile

testFile = "../../Templates/TestFileTemplate.test"
IDFile = "../../Templates/IDFileTemplate.test"
participantFile = "../../Templates/participant.list"

def cleanup(folder):
	for files in os.listdir(folder):
		filePath = os.path.join(folder, files)
		try:
			if os.path.isfile(filePath):
				os.unlink(filePath)
			elif os.path.isdir(filePath):
				shutil.rmtree(filePath)
		except Exception as e:
			print(e)
	shutil.rmtree(folder)
	
f = ""

if(create.createFilesystem(f)):
	print "Failed to detect empty inputs"
	exit(-1)

f = readTestFile.readFile(testFile)

if(not create.createFilesystem(f)):
	print ("Failed with loaded files. Check file names and if correct," 
	" algorithm has errors.")
	cleanup('./Test Name/')
	exit(-1)

cleanup('./Test Name/')

f = readTestFile.readFile(IDFile)

if(not create.createFilesystem(f)):
	print ("Failed with ID file. Check file names and if correct,"
	"algorithm has errors.")
	cleanup('./TestIDs/')
	exit(-1)

print "Pass"
cleanup('./TestIDs/')
