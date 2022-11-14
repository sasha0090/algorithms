"""
Гоша реализовал структуру данных Дек, максимальный размер которого определяется
заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно.
Но, если в деке было много элементов, программа работала очень долго.
Дело в том, что не все операции выполнялись за O(1). Помогите Гоше!
Напишите эффективную реализацию.
"""


class Deque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.deque_size = 0

    def size(self):
        return self.deque_size

    def is_full(self):
        return self.deque_size == self.max_size

    def is_empty(self):
        return self.deque_size == 0

    def push_back(self, value):
        if self.is_full():
            raise LookupError('Дека полная')

        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.deque_size += 1

    def push_front(self, value):
        if self.is_full():
            raise LookupError('Дека полная')

        self.deque[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.deque_size += 1

    def pop_back(self):
        if self.is_empty():
            raise LookupError('Дека пустая')

        tail_deque = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.deque_size -= 1
        return tail_deque

    def pop_front(self):
        if self.is_empty():
            raise LookupError('Дека пустая')

        head_deque = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.deque_size -= 1
        return head_deque


def solution(deque_max_size, commands):
    results = []
    deque = Deque(deque_max_size)
    for command, *args in commands:
        try:
            command_result = getattr(deque, command)(*args)
            if command_result:
                results.append(command_result)
        except LookupError:
            results.append('error')

    return results


def read_input():
    command_amount = int(input())
    max_size = int(input())
    commands = [input().split(' ') for _ in range(command_amount)]
    return max_size, commands


if __name__ == '__main__':
    deque_max_size, commands = read_input()
    print('\n'.join(solution(deque_max_size, commands)))
