def readFile(filename):
	contents = {}
	try:
		with open(filename, 'r') as f:
			contents['FileName'] = filename
			for line in f:
				splitLine = line.rstrip().split(': ')
				if ', ' in splitLine[1]:
					splitLine[1] = splitLine[1].split(', ')
				contents[splitLine[0]] = splitLine[1]
		return contents
	except(IOError):
		return False
