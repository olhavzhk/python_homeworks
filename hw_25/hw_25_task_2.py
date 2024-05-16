class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(sequence):
    stack = Stack()
    matching_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for char in sequence:
        if char in matching_pairs.keys():
            stack.push(char)
        elif char in matching_pairs.values():
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return "not balanced"

    if stack.is_empty():
        return "balanced"
    else:
        return "not balanced"
