def outer_function():
    def inner_function():
        print("inner function")
    return inner_function


func = outer_function()

func()
