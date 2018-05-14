import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):

	word = word.lower()

	if word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0:
		print("Did you mean %s instead? Type Y for yes or N for no: "   %  get_close_matches(word, data.keys())[0])
		response = input("")
		if response == 'Y':
			return data[get_close_matches(word, data.keys())[0]]
		elif response == 'N':
			return "The word doesn't exist. Please double check."
		else:
			return "We didn't understand your response."
	else:
		return "The word doesn't exist. Please double check."

word = input("Enter word: ")

output = translate(word)


if type(output) == list:
	for item in output:
		print(item)

else:
	print(output)
