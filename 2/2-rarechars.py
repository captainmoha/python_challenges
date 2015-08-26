import string
punc = string.punctuation
letters = string.ascii_letters
message = ""
mess = open("C:/Users/Moha/Desktop/Spass/Python/challenges/2/hotmess.txt","r")
for line in mess:
	haystack = [str(c) for c in line]
	for letter in letters:
		if letter in haystack:
			message += letter
print message