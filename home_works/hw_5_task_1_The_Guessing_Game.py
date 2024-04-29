import random

player_number = input("Please, insert a number between 1 and 10: ")

random_number = random.choice(range(1, 11))
if int(player_number) == random_number:
    print("The random number is :", str(random_number), "\nYou guessed the number!")
else:
    print("The random number is :", str(random_number), "\nTry again!")
