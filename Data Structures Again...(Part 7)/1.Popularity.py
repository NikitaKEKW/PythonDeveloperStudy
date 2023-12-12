import re

text = "hello, word of word"
words_popularity = {}
chars_popularity = {}

for char in text:
    chars_popularity[char] = chars_popularity.setdefault(char, 0) + 1
print('Популярность букв:', chars_popularity)

splitted_text = re.split(r'[., ]', text)
for word in text.split():
    words_popularity[word] = words_popularity.setdefault(word, 0) + 1
print('Популярность слов: ', words_popularity)
