# read me contents
# welcome to my zipped list.

# hint1: start from 90052
# hint2: answer is inside the zip

import re, zipfile
# keep log of of nothings and count
def log(nothing, count):
	logFile = open('log.txt', 'a')
	logFile.write("Count: " + str(count))
	logFile.write("\nCurrent_nothing" + str(nothing))
	logFile.write("\n\n___________________________________________\n\n")
	logFile.close()
	
# try to find the answer in files
def findAns():
	FILES_LOCATION = '/home/jharvard/spass/python/python_challenges/6/zip/'
	regex = r"nothing is (\d+)"
	current_nothing = '90052'
	count = 0

	while (count <= 910):
		current_nothing_file = FILES_LOCATION + current_nothing + ".txt"
		get_file  = open(current_nothing_file, 'r').read()
		current_nothing = re.search(regex, str(get_file)).group(1)
		log(current_nothing, count)
		count += 1
	
#findAns()

# findAns terminates with an attribute error meaning that it has found a file that has no number (no nothing)
# inspecting the file that caused the error resulted in find the following text : "Collect the comments"
# hmm I need to think differently
# after some thinking and reading I think I can get the comments with the help of zipfil module let's do that.

def findAns2():
	channelZip = zipfile.ZipFile('channel.zip')
	comments = open('comments.txt', 'w')
	regex = r"nothing is (\d+)"
	current_nothing = '90052'
	count = 0
	zippedFilesList = channelZip.namelist()
	
	while (count <= len(zippedFilesList)):
		# get comment and write it to a file
		cuurent_file = current_nothing + '.txt'
		comment = channelZip.getinfo(cuurent_file).comment
		comments.write(str(comment))
		# get the next nothing and move to the next file
		file_content = channelZip.read(cuurent_file)
		current_nothing = re.search(regex, str(file_content)).group(1)
		
	# close comments file
	comments.close()
	
# wohoo solved!
findAns2()
