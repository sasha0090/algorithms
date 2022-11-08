class StackMax:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, num: int):
        self.items.append(num)

    def pop(self):
        self.items.pop()

    def get_max(self):
        return max(self.items)


def read_input():
    n = int(input())
    commands = [input().split(' ') for _ in range(n)]
    return commands


def solution(commands):
    stack = StackMax()
    for command in commands:
        if command[0] == 'get_max':
            if stack:
                print(stack.get_max())
            else:
                print('None')
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack:
                stack.pop()
            else:
                print('error')


if __name__ == '__main__':
    commands = read_input()
    solution(commands)
