import random

first_value = random.randint(0, 10)
second_value = random.randint(0, 10)

answer = input(str(first_value) + "+" + str(second_value) + "=")

if int(answer) == first_value + second_value:
    print("Correct!")
else:
    print("Hmm.. Looks like your answer isn't quite correct.")
