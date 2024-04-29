def in_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("Step can not be zero")
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        while start < end:
            yield start
            start += step


print(list(range(0, 10, 1)))
print(list(in_range(0, 10, 1)))
