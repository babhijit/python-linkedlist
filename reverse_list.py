"""
Reverses a singly linked list
"""

from linked_list import LinkedList, Node


def reverse_list(linked_list: LinkedList, use_recursion=False):
    if use_recursion:
        tail, head = rev_list_rec(linked_list.head)
        if tail:
            tail.next = None
        linked_list.head = head
    else:
        linked_list = rev_list_iter(linked_list)
    return linked_list


def rev_list_rec(current: Node):
    if current:
        if current.next:
            tail, head = rev_list_rec(current.next)
            tail.next = current
            return current, head
    return current, current     # last node will always be head node for reversed list


def rev_list_iter(linked_list: LinkedList):
    if linked_list.head and linked_list.head.next:
        prev = None
        current = linked_list.head
        while current:
            rest = current.next
            current.next = prev
            prev = current          # previous is now the new head
            current = rest
        linked_list.head = prev
    return linked_list


if __name__ == '__main__':
    llist = LinkedList()

    for i in range(10, 0, -1):
        llist.push(i)

    llist = reverse_list(llist, True)

    print('The number of nodes', llist.size())
