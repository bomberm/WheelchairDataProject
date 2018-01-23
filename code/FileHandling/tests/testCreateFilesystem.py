import sys, os, shutil
sys.path.append("../")
import createFilesystem as create

testFile = "../../Templates/TestFileTemplate.test"
participantFile = "../../Templates/participant.list"

def cleanup():
	folder = './Test Name/'
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
g = "" 

if(create.createFilesystem(f, g)):
	print "Failed to detect empty inputs"
	exit(-1)

f = open(testFile, "r")

if(create.createFilesystem(f,g)):
	print "Failed to detect empty particpant list"
	cleanup()
	exit(-1)

g = open(participantFile, "r")

if(not create.createFilesystem(f, g)):
	print ("Failed with loaded files. Check file names and if correct," 
	" algorithm has errors.")
	exit(-1)

print "Pass"
#cleanup()
