# Write a decorator arg_rules() that validates arguments passed to the function.
#
# A decorator should take 3 arguments:
#
# max_length: 15
#
# type_: str
#
# contains: [] - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed; otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if not all(isinstance(arg, type_) for arg in args):
                print("The type of argument should be: ", type_)
                return False
            if not all(len(arg) <= max_length for arg in args):
                print("The argument shouldn't be longer than", max_length, "characters")
                return False
            for arg in args:
                if not all(symbol in arg for symbol in contains):
                    print("Arguments must contain all of the following symbols:", contains)
                    return False
            return function(*args, **kwargs)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
