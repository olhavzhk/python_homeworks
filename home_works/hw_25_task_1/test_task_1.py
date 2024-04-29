import pytest
from task_1 import (
    BaseSequence,
    Stack,
    Deque
)


def test_put():
    stack_2 = BaseSequence([1, 2, 'a'])
    stack_2.put("1")
    assert stack_2.storage == [1, 2, 'a', '1']


def test_is_empty():
    stack_2 = BaseSequence([])
    assert stack_2.is_empty() == True


def test_is_full():
    stack_2 = BaseSequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert stack_2.is_full() == True


def test_pop():
    stack_1 = Stack([1, 2, 3])
    stack_1.pop()
    assert stack_1.storage == [1, 2]


def test_peek():
    stack_1 = Stack([1, 2, 3])
    assert stack_1.peek() == 3


def test_appendleft():
    deque_1 = Deque([1, 2, 3, 4])
    deque_1.appendleft(0)
    assert deque_1.storage == [0, 1, 2, 3, 4]


def test_popleft():
    deque_1 = Deque([1, 2, 3, 4])
    deque_1.popleft()
    assert deque_1.storage == [2, 3, 4]


if __name__ == "__main__":
    pytest.main()
