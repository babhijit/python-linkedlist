"""
Utilities for Linked List that can be used by py.test
"""

from linked_list import LinkedList
from random import randint


def populate_list(number_or_nodes):
    llist = LinkedList()
    for i in range(0, number_or_nodes):
        llist.push(randint(0, 9))
    return llist

