import os

current_dir = os.path.dirname(os.path.abspath(__file__))
mymod = os.path.join(current_dir, "mymod.py")


code = """
def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)


def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines in file is {lines}")
    print(f"Number of characters in file is {chars}")
"""

with open(mymod, "w") as file:
    file.write(code)

print(f"File was created with three functions in it.")


import mymod

mymod.test(input("Provide a file name: "))




