# input : "CAT BAT MAT CAT MAT CAT"
# output : "CAT 3 BAT 1 MAT 2"

def countWords(s):
	wordCount = dict()
	words = s.split(" ")

	for word in words:
		if word in wordCount:
			wordCount[word] += 1
		else:
			wordCount[word] = 1

	result = ""
	for word in wordCount:
		result += word + " " + str(wordCount[word]) + " "

	return result[:len(result)-1]

s = "CAT BAT MAT CAT MAT CAT"
print(countWords(s))
