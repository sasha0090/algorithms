"""
Задание связано с обратной польской нотацией.
Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.

В постфиксной нотации операнды расположены перед знаками операций.

Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * -
означает 10 - 2 * 4 и равно 2

Разберём последний пример подробнее:

Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию,
которую этот знак обозначает, то есть перемножить эти два числа. В результате получим 8.

После этого выражение приобретёт вид:

10 8 -

Операцию «минус» нужно применить к двум идущим перед ней числам, то есть 10 и 8
В итоге получаем 2.

Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.

Для вычисления значения выражения, записанного в обратной польской нотации,
нужно считывать выражение слева направо и придерживаться следующих шагов:

Обработка входного символа:
Если на вход подан операнд, он помещается на вершину стека.
Если на вход подан знак операции, то эта операция выполняется над требуемым
количеством значений, взятых из стека в порядке добавления.
Результат выполненной операции помещается на вершину стека.
Если входной набор символов обработан не полностью, перейти к шагу 1.
После полной обработки входного набора символов результат вычисления выражения
находится в вершине стека. Если в стеке осталось несколько чисел,
то надо вывести только верхний элемент.
Замечание про отрицательные числа и деление: в этой задаче под делением
понимается математическое целочисленное деление.
Это значит, что округление всегда происходит вниз.
А именно: если a / b = c, то b ⋅ c — это наибольшее число, которое не
превосходит a и одновременно делится без остатка на b.

Например, -1 / 3 = -1. Будьте осторожны: в C++, Java и Go, например, деление
чисел работает иначе.

В текущей задаче гарантируется, что деления на отрицательное число нет.

"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elm):
        self.stack.append(elm)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise IndexError('Стек пустой')


def solution(postfix_notation, stack):
    operators = {
        '+': lambda a, b: b + a,
        '-': lambda a, b: b - a,
        '*': lambda a, b: b * a,
        '/': lambda a, b: b // a,
    }

    for elm in postfix_notation:
        if elm in operators.keys():
            a, b = int(stack.pop()), int(stack.pop())
            stack.push(operators[elm](a, b))
        else:
            stack.push(elm)

    return stack.pop()


if __name__ == '__main__':
    postfix_notation = input().split(' ')
    stack = Stack()

    print(solution(postfix_notation, stack))
