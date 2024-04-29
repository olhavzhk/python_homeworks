# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError


try:
    oops()
except IndexError:
    print("IndexError was caught")

# If we change oops to raise KeyError instead of IndexError, our code will break on lane 10.
