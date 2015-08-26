import re
regex = r"([a-zA-Z]+) (\d+)"
new_regex = r"\2 of \1"
string = "jan 24, aug 20 this is not a car it is a jun 29"

def findSingle(string, regex):
	"""
	Finds the first occurance of a string using regex
	string: a string 
	regex: regex pattern
	"""
	# re.search(pattern, input_str, flags=0) only finds the first match it finds
	if re.search(regex,string):
	    match = re.search(regex, string)
	    print "Match at index %s, %s" % (match.start(), match.end())
	    print "Full Match:  %s" % (match.group(0))
	    print "Month: %s" % (match.group(1))
	    print "Day: %s" % (match.group(2))
	else:
	    print "NOthing found"

def findGroups(string, regex):
	"""
	Finds the group of matches from a string using regex
	string: a string
	regex: regex pattern
	"""
	# re.findall(pattern, input_str, flags=0) returns a list of matches
	if re.findall(regex, string):
		count = 1
		matches = re.findall(regex, string)
		for match in matches:
			match = " ".join(match)
			print "%d-" % count,match
			count += 1
	else:
		print "NOthing found"

def findNReplace(string, init_regex, new_regex):
	"""
	Finds and replaces a substring in a string using regex
	"""
	# re.sub(pattern, replacement_pattern, input_str, count, flags=0)
	# replaces a substring in a string
	init_regex = regex
	new_regex = new_regex
	print string
	newString = re.sub(init_regex, new_regex, string)
	print newString