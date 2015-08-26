import string 
text = "jkfeiauzroivgzbmpszazlutnwsdofbiawqivdjnbzsyhfcrblqgusbydajayagcbjcwggtdmfjeptobhcmdlzxajvvgithekczgtpkcfwqbvkoixetpiiljanvvqjjgitcpadzjkgcbluaidgumcdskunuijfwcjhfmbzpkzsbajsdxsqqdqlaeisjezfjfdaoljapkywxjthqjknnedznxhnsahxqedoeqsdcmtmltcqsnwakjxdtytfaalyhlgaibekfmyiimwrkffydghiunlzriwgmkuzmnqcljjbesxguytfsatejmdwkbfbzifdknplcqimvehxujkszbuyutmsompijcjojspbywlroefiwmqrsjstdjhgfwxhcnthsoxosmjoqtufoxvpvpjkgiaqgofrhyuflxxdnjiwtfquqsbkdeakunqjgdkfnxdpifbulklgjougnivhgixsnekoxjgrirbsllpuaouvhzabilbjirmqdqrxftktgcnkdljcoasnexwtgvwjaehgurngksokjtromovpcmygkzgevolwynsyfideomflmkwmj"
def decrept(text):
	message = ""
	letters = string.ascii_letters
	punc = string.punctuation
	dictLetters = {}
	for letter in letters:
		dictLetters[letter] = letters[(letters.index(letter) + 2) % 52]
	for char in text:
		if char in dictLetters:
			message += dictLetters[char]
		elif char == " ":
			message += " "
		elif char in punc:
			message += char
	return message.lower()


# message = i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print decrept(text)