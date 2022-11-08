"""
Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size,
означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
очереди. Функции, которые надо поддержать, описаны в формате ввода.
"""
import sys


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, x):
        if self.queue_size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.queue_size += 1

    def pop(self):
        if self.queue_size == 0:
            return None

        head_queue = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.queue_size -= 1
        return head_queue

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.queue_size


def solution(queue_max_size, commands):
    result = []
    queue = MyQueueSized(queue_max_size)
    for command in commands:
        queue_size = queue.size()
        if command[0] == 'push':
            if queue_size >= queue_max_size:
                result.append('error')
            else:
                queue.push(command[1])

        elif command[0] == 'pop':
            if queue_size == 0:
                result.append('None')
            else:
                result.append(queue.pop())

        elif command[0] == 'peek':
            if queue_size == 0:
                result.append('None')
            else:
                result.append(queue.peek())

        elif command[0] == 'size':
            result.append(str(queue_size))
    return result


def read_input():
    command_amount = int(input())
    max_size = int(input())
    commands = [sys.stdin.readline().strip().split(' ')
                for _ in range(command_amount)]
    return max_size, commands


if __name__ == '__main__':
    queue_max_size, commands = read_input()
    print('\n'.join(solution(queue_max_size, commands)))
