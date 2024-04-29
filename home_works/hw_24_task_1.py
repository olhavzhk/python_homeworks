from typing import Union
# I used Union instead module of Optional, because with Optional I got this error message:
# TypeError: typing.Optional requires a single type. Got (<class 'int'>, <class 'float'>).


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    elif exp == 0:
        return 1
    elif exp == 1:
        return x
    else:
        return x * to_power(x, exp - 1)
