import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "myfile.txt")


code = """
Hello file world!\n
"""
with open(file_path, "w") as file:
    file.write(code)
    # print(f"File was created.")


with open(file_path, "r") as file:
    print(type(file.read()))


