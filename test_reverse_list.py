from unittest import TestCase
from linked_list import LinkedList
from random import randint, randrange
import reverse_list


def populate_list(number_or_nodes):
    llist = LinkedList()
    for i in range(0, number_or_nodes):
        llist.push(randint(0, 9))
    return llist


class TestReverse_list(TestCase):
    def test_reverse_list_iter_empty(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=False)
        self.assertEquals(llist.size(), 0)

    def test_reverse_list_rec_empty(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=True)
        self.assertEquals(llist.size(), 0)

    def test_reverse_list_iter_one(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=False)
        self.assertEquals(str(llist), str(rev_llist))

    def test_reverse_list_rec_one(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=True)
        self.assertEquals(str(llist), str(rev_llist))

    def test_reverse_list_iter_even(self):
        llist = populate_list(randrange(2, 20, 2))
        llist_str = str(llist)
        rev_llist = reverse_list.reverse_list(llist, use_recursion=False)
        self.assertEquals(llist_str, str(rev_llist)[-1::-1])

    def test_reverse_list_rec_odd(self):
        llist = populate_list(randrange(1, 19, 2))
        llist_str = str(llist)
        rev_llist = reverse_list.reverse_list(llist, use_recursion=True)
        self.assertEquals(llist_str, str(rev_llist)[-1::-1])
