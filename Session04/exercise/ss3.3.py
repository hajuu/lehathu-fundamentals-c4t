from random import *
words=['python','loneli','bich ngoc','dinh quy']
word=choice(words)
letters=list(word)
shuffle(letters)
scrambled=' '.join(letters)
print(scrambled)

answer=input("ur answer:")
while answer != word:
    answer=input("try again:")

print(":)")