
from random_word import RandomWords
from random_word import Wordnik
r = RandomWords()
print(r.get_random_word())

ran_words = Wordnik()

print(ran_words.get_random_words(includePartOfSpeech="proper-noun", minLength=5, maxLength=15, sortBy='alpha', sortOrder='asc', limit=5))

