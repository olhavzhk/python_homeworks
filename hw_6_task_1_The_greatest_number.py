import random

list_of_numbers = []

while len(list_of_numbers) < 10:
    list_of_numbers.append(random.randint(0, 10))


print(max(list_of_numbers))
