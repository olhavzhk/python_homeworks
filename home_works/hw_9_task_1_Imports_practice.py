import os

path = "./new_directory/"
os.mkdir(path)

module1 = "file1.py"
module2 = "file2.py"

module_path = os.path.join(path, module1)

with open(module_path, "w") as module:
    module.write("def printing_function(text):\n    print(text)\n")
print("module 1 is created")

module_path = os.path.join(path, module2)
with open(module_path, "w") as module:
    module.write("import file1\nimported_function = file1.printing_function('it works')\n")
print("module 2 is created")

