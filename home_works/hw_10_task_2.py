# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def numbers_input():
    a = float(input("Provide the first number: "))
    b = float(input("Provide the second number: "))
    print(a**2 / b)


try:
    numbers_input()
except ValueError:
    print("wrong input, it should contain only digits and (optionally) dots")
except ZeroDivisionError:
    print("you can not divide by zero")

