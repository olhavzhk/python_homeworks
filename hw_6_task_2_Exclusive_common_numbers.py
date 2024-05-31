import random

first_list = []
second_list = []
third_list = []


while len(first_list) < 10 and len(second_list) < 10:
    first_list.append(random.randint(0, 10))
    second_list.append(random.randint(0, 10))

third_list = set(first_list + second_list)

print(first_list)
print(second_list)
print(third_list)
