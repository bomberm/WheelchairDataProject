import json
from pathlib2 import Path

fileName = '../Templates/Chiron.json'

checkIfExists = Path(fileName)
if checkIfExists.is_file:
	testFile = checkIfExists.open()
else:
	raise IOError('Some Error')

data = json.load(testFile)

for line in data:
	print line+' '+str(data[line])
