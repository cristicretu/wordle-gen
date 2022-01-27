import requests
from random import randrange

response = requests.get('https://raw.githubusercontent.com/cristicretu/wordle/main/index.js')

index = response.text

words = ''.join(index.splitlines(keepends=True)[3:])

words = words[:words.find(']')]

words_array = words.replace(' ', '').replace(',', '').replace("'", "").split('\n')

words_array.pop()

with open('result.txt', 'w') as f:
		f.write(words_array[randrange(0, len(words_array))])