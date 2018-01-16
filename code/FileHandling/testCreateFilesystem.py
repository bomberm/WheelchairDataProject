import createFilesystem as create
import os, shutil

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
	
f = ""
g = "" 

if(create.createFilesystem(f, g)):
	print "Failed to detect empty inputs"
	exit(-1)

f = open("../Templates/TestFileTemplate.test", "r")

if(create.createFilesystem(f,g)):
	print "Failed to detect empty particpant list"
	cleanup()
	exit(-1)

g = open("../Templates/participant.list", "r")

if(not create.createFilesystem(f, g)):
	print ("Failed with loaded files. Check file names and if correct," 
	" algorithm has errors.")
	exit(-1)

print "Pass"
cleanup()
shutil.rmtree('./Test Name')
