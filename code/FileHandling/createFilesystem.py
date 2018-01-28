import os, errno, shutil

def createFilesystem(testFile, participantFile):
	#get directory name
	if not type(testFile) is dict:
		return False 

	dirName = testFile['Name']
	dirName = dirName.strip()

	#Create 'root' of test storage
	if not os.path.exists(dirName):
		os.makedirs(dirName)
	else:
		#handle editing current dir
		print 'Filesystem exists' #remove print once real functionality is added

	#Begin populating storage directory
	shutil.copy(testFile['FileName'], './'+dirName+'/')	
	

	#Test Participant Data - This will need to be updated to include logic for IDs
	if not 'Participant Data' in testFile:
		return False
	
	if not hasattr(participantFile, 'readline'):
		return False

	#Set up for security
	if int(testFile['Secure']) == 1:
		secure = True
	
	#Create subDirs for each participant
	for name in participantFile:
		if not os.path.exists(name.rstrip()):
			os.makedirs(dirName+'/'+name.rstrip()+'/')

	return True	
