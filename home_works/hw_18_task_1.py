def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1


name = "Olha"

print(list(with_index(name)))
