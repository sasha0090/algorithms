"""
Вася размышляет, что ему можно не делать из того списка дел,
который он составил.
Но, кажется, все пункты очень важные!
Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка.
Напишите функцию solution, которая принимает на вход голову списка и номер
удаляемого дела и возвращает голову обновлённого списка.

"""
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item
    index = 0
    head = node
    while True:
        if index == idx-1:
            node.next_item = node.next_item.next_item
            break
        node = node.next_item
        index += 1
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()