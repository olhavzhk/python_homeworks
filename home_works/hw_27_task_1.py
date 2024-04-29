import string


ASCII_MAPPING = {}
INDEX = 0
for letter in string.ascii_letters + "0123456789 ,.!?()[]":
    ASCII_MAPPING[letter] = INDEX
    INDEX += 1


def hash_function(key: str, size=100):
    """Take a key as an input and calculate an integer output.
    Output should be between 0 and size
    """
    key = str(key)
    hash_value = 0
    for letter in key:
        hash_value += ASCII_MAPPING[letter]
    hash_value = hash_value % size
    return hash_value


class Dictionary:
    def __init__(self):
        self._capacity = 10
        self.size = 0
        self.storage = []
        self._resize_and_rehash()

    def _resize_and_rehash(self):
        old_storage = self.storage.copy()
        self._capacity *= 2
        self.storage = []
        for _ in range(self._capacity):
            self.storage.append([])

        for cell in old_storage:
            for key, value in cell:
                self.put(key, value)

    def get(self, search_key):
        index = hash_function(search_key, size=self._capacity)
        for key, value in self.storage[index]:
            if search_key == key:
                return value
        raise KeyError(search_key)

    def put(self, key, value):
        self.size += 1
        if self.size == self._capacity:
            self._resize_and_rehash()
        index = hash_function(key, size=self._capacity)
        self.storage[index].append((key, value))

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.storage})"

    def keys(self):
        keys = []
        for item in self.storage:
            for key, _ in item:
                keys.append(key)
        return keys

    def pop(self, search_key):
        index = hash_function(search_key, size=self._capacity)
        item = self.storage[index]
        for i, (key, value) in enumerate(item):
            if search_key == key:
                del item[i]
                return value

    def items(self):
        items = []
        for item in self.storage:
            for key, value in item:
                items.append((key, value))
        return items


demo_dict = Dictionary()
demo_dict["1"] = 1
print(demo_dict["1"])
demo_dict["2"] = 2
demo_dict[(1, 2, 3)] = (1, 2, 3)
print(demo_dict.storage)
demo_dict.pop("2")
print(demo_dict.storage)
print(demo_dict.keys())
print(demo_dict.items())
print(repr(demo_dict))
