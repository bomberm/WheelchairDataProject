import os, errno, shutil

def createFilesystem(testFile, participantFile):
	if not hasattr(testFile, 'readline'): #check if passed variable is file-like
		return False
	
	#get directory name
	testFile.seek(0) #ensure we are at top of file
	dirName = testFile.readline()
	dirName = dirName.split(": ")[1].rstrip()

	#Create 'root' of test storage
	if not os.path.exists(dirName):
		os.makedirs(dirName)
	else:
		#handle editing current dir
		print 'Filesystem exists' #remove print once real functionality is added

	#Begin populating storage directory
	shutil.copy(testFile.name, './'+dirName+'/')	
	

	#Test Participant Data
	if not hasattr(participantFile, 'readline'):
		return False
	
	#Create subDirs for each participant
	for name in participantFile:
		if not os.path.exists(name.rstrip()):
			os.makedirs(dirName+'/'+name.rstrip()+'/')

	return True	
