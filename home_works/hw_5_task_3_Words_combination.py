from random import shuffle

users_word = input("Please provide a word: ")

for _ in range(5):
    users_word = list(users_word)
    shuffle(users_word)
    users_word = ''.join(users_word)
    print(users_word)
