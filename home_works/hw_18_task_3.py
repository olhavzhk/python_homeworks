class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            iterable_item = self.iterable[self.index]
            self.index += 1
            return iterable_item
        else:
            raise StopIteration

    def __getitem__(self, index):
        if 0 <= index <= len(self.iterable):
            return self.iterable[index]


my_list = list(range(10))
my_list = MyIterable(my_list)

for item in my_list:
    print(item)

print(my_list[0])
