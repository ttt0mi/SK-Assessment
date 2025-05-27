def encrypt(sentence):

	alphabets = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
b
	new_sentence = list(sentence)

	for index, char in enumerate(sentence):
		if sentence[index].isalpha:
			sentence = sentence.replace(sentence[index], alphabets[index + 26], 1) 


	return sentence




sample = "abc, defg"

print(encrypt(sample))