import string
import re

# useless first attempt without regex
message = ""
oneBetweenThree = open("C:/Users/Moha/Desktop/Spass/Python/challenges/3/smallsuroundedbyBIG.txt","r")
def isSmall(char):
	small = string.ascii_lowercase
	if char in small:
		return True
	else:
		return False
# useless function
def findIt(fileHandle):
	lista = []
	for line in fileHandle:
		line = line.rstrip()
		tempMap = {}
		letters = [str(l) for l in line]
		for index in range(len(letters)):
			tempMap[index] = letters[index]

		for key, char in tempMap.items():
			count = 0
			temp = []
			if isSmall(char):
				temp.insert(0,tempMap[(key - 3) % len(line)])
				temp.insert(1,tempMap[(key - 2) % len(line)])
				temp.insert(2,tempMap[(key - 1) % len(line)])
				temp.insert(3,tempMap[key])
				temp.insert(4,tempMap[(key + 1) % len(line)])
				temp.insert(5,tempMap[(key + 2) % len(line)])
				temp.insert(6,tempMap[(key + 3) % len(line)])
				if (not isSmall(temp[0]) and not isSmall(temp[1]) and not isSmall(temp[2]) and not isSmall(temp[4]) and not isSmall(temp[5]) and not isSmall(temp[6])):
					
					message = "".join(temp)
					lista.append(message)
	return lista

# this one turned out to be useful :D
def build(findIt):
	message = ""
	for item in findIt:
		message += str(item[3])
	return message

# solution using regex which is awesome!
regex = r"([A-Z]{3}[a-z][A-Z]{3})"
regex = r'[^A-Z]([A-Z]{3}[a-z][A-Z]{3})[^A-Z]'
result = []
def regexa(regex, fileHandle):
	fileToString = fileHandle.read()
	result = "".join(build(re.findall(regex, fileToString)))
	return result





