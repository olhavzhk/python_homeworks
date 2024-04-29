def local_variable_counter(func):
    local_var_dict = func.__code__.co_varnames
    print(f"The function {func.__name__} has {len(local_var_dict)} local variables.")


def some_function():
    first_var = 1
    second_var = 3
    third_var = 4
    result = first_var + second_var - third_var
    return result


local_variable_counter(some_function)
