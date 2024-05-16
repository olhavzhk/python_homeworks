from functools import wraps


def check_full(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_full():
            raise ValueError("storage full")
        return method(self, *args, **kwargs)

    return wrapper


def check_empty(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_empty():
            raise ValueError("storage empty")
        return method(self, *args, **kwargs)

    return wrapper


class BaseSequence:
    def __init__(self, initial_items: list, capacity=10):
        self.storage = initial_items
        self.capacity = capacity

    @check_full
    def put(self, element):
        if self.is_full():
            raise ValueError("storage full")
        self.storage.append(element)

    def is_empty(self):
        return not bool(self.storage)

    def is_full(self):
        return len(self.storage) == self.capacity


class Stack(BaseSequence):
    """Data structure that is a sequence of items with the following methods:
    LIFO - last in, first out
    push(item) - place an item on top of the stack
    pop - remove item from the top of the stack
    is_empty - return a bool
    is_full - return a bool depending on maximum capacity
    peek - get an item from the top, but do not remove it
    """
# changed name of method "put" to "push" that is associated with stack

    @check_empty
    def pop(self):
        if self.is_empty():
            raise ValueError("storage empty")
        return self.storage.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("storage empty")
        return self.storage[-1]


stack_1 = Stack([1, 2, 3])
print(stack_1.storage)
stack_1.put(4)
print(stack_1.storage)
print(stack_1.peek())
print(stack_1.pop())
print(stack_1.pop())


class Queue(BaseSequence):
    """Data structure that is a sequence of items with the following methods:
    FIFO - first in, first out
    put - place an item on top of the queue
    get - remove item from the top of the queue
    empty - return a bool
    full - return a bool depending on maximum capacity
    """
# changed description of "get" method, since it remove item from the top, not the bottom of the Queue
# added methods:
#     put_nowait(item) – Put an item into the queue without blocking.
#                         If no free slot is immediately available, raise QueueFull.
#     get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
#     qsize() – Return the number of items in the queue.
#     maxsize – Number of items allowed in the queue.


# moved the "get_beginning" function from Queue to the Deque class,
# as Queue class should have one simple "get" method,
# since items in the Queue class can be removed only from one side - top.


class Deque(Queue):
    """
    Data structure that is a sequence that allows you to put and remove items from both ends
    """
# removed Stack from Deque parent classes, as Dequeue will inherit Stack methods through Queue inheritance.


# changed names of functions "put_beginning" and "get_beginning" to "appendleft" and "popleft"
    @check_full
    def appendleft(self, element):
        self.storage.insert(0, element)

    def popleft(self):
        return self.storage.pop(0)
