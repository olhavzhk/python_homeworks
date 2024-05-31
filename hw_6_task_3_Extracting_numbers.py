full_list = list(range(1, 101))
number = 1
extracted_numbers_list = full_list.copy()


while number <= 100:
    if not number % 7 == 0 or number % 5 == 0:
        extracted_numbers_list.remove(number)
    number += 1

print(extracted_numbers_list)
print(full_list)
