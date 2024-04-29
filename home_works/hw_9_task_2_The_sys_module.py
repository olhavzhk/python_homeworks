# You can modify the sys.path list manually if needed from within Python.
# It is just a regular list, so it can be modified in all the normal ways.
# For example, you can append to the end of the list using sys.path.append()
# or to insert in an arbitrary position using sys.path.insert().

import sys
print(sys.path)

sys.path.append('C:\\new_file1.txt')
sys.path.insert(0, 'C:\\newfile.py')

print(sys.path)
