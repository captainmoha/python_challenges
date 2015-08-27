import urllib, re
def followNothings():
	"""
	follows urls based on numbers in the page source
	saves log of counter and "nothing" values
	"""
	counter = 0
	regex = r"(\d+)"
	currentNothing = 12345
	# keep results in a file
	txt = open("nothings_log.txt", "w")
	while (counter <= 400):
		get_src = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(currentNothing))
		src_text = str(get_src.read())
		txt.write("current nothing: " + str(currentNothing))
		txt.write("\n")
		txt.write("counter: " + str(counter))
		txt.write("\n_________________________________________\n\n")
		currentNothing = re.search(regex, src_text).group(0)
		counter += 1
	txt.close()

# after running the followNothings it terminates with an AttributeError because it found no number in a page's source
# checking the url using the last value of currentNothing variable found in nothings_log.txt I found the following instruction
# "Yes. Divide by two and keep going."

# next phase reinitializing currentNothing according to the instruction ie 16044/2
def followNothings2():
	"""
	follows urls based on numbers in the page source
	saves log of counter and "nothing" values
	"""
	counter = 0
	regex = r"(\d+)"
	currentNothing = 16044/2
	# keep results in a file
	txt = open("nothings_log2.txt", "w")
	while (counter <= 400):
		get_src = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(currentNothing))
		src_text = str(get_src.read())
		currentNothing = re.search(regex, src_text).group(0)
		counter += 1
		txt.write("current nothing: " + str(currentNothing))
		txt.write("\n")
		txt.write("counter: " + str(counter))
		txt.write("\n")
		txt.write("_________________________________________")
		txt.write("\n")
	txt.close()

# after running followNothings2 it terminates with an AttributeError as well checking the log and using the currentNothing value
#  to follow the url I got the following instruction
# "You've been misleaded to here. Go to previous one and check."
# this is getting interesting. I guess I need to sharpen my regex

def followNothings3():
	"""
	follows urls based on numbers in the page source
	saves log of counter and "nothing" values
	"""
	counter = 0
	regex = r"the next nothing is (\d+)|the next nothing (\d+)"
	currentNothing = 16044/2
	# keep results in a file
	txt = open("nothings_log3.txt", "w")
	while (counter <= 400):
		get_src = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(currentNothing))
		src_text = str(get_src.read())
		currentNothing = re.search(regex, src_text).group(1)
		print currentNothing
		counter += 1
		txt.write("current nothing: " + str(currentNothing))
		txt.write("\n")
		txt.write("counter: " + str(counter))
		txt.write("\n")
		txt.write("_________________________________________")
		txt.write("\n")
	txt.close()

# after running followNothings3 it terminates with the usual AttributeError. Checking the log and using currentNothing value to follow the url I got the following
# "peak.html" 
# SOLVED!
