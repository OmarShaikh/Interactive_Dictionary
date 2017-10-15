import json
from difflib import get_close_matches

data = json.load(open('data.json','r'))

def translator(word):
	word=word.lower()
	if word in data:
		return data[word][0]
	elif len(get_close_matches(word,data.keys())) > 0:
		ch=input('Did you mean %s instead? (Y|N):' % get_close_matches(word,data.keys())[0])
		if ch=='Y'or ch=='y':
			return data[get_close_matches(word,data.keys())[0]][0]
		elif ch=='N' or ch=='n':
			return "Sorry, word does not exist!"
		else:
			return 'Invalid Choice!'

	else:
		return "Word doesn't exist. Try again!"

word=input('Enter the word: ')
print(translator(word))
