"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.
"""

import sys


class StackMaxEffective:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, num: int):
        if not self.items or self.items[-1] < num:
            self.items.append(num)
        else:
            self.items.append(self.items[-1])

    def pop(self):
        self.items.pop()

    def get_max(self):
        return self.items[-1]


def read_input():
    n = int(input())
    commands = [sys.stdin.readline().strip().split(' ') for _ in range(n)]
    return commands


def solution(commands):
    result = []
    stack = StackMaxEffective()
    for command in commands:
        if command[0] == 'get_max':
            if stack:
                result.append(str(stack.get_max()))
            else:
                result.append('None')
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack:
                stack.pop()
            else:
               result.append('error')
    print('\n'.join(result))


if __name__ == '__main__':
    commands = read_input()
    solution(commands)
