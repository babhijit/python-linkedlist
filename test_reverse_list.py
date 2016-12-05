from unittest import TestCase
from linked_list import LinkedList
from random import randrange
import list_utils
import reverse_list



class TestReverse_list(TestCase):
    def test_reverse_list_iter_empty(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=False)
        self.assertEquals(rev_llist.size(), 0)

    def test_reverse_list_rec_empty(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=True)
        self.assertEquals(rev_llist.size(), 0)

    def test_reverse_list_iter_one(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=False)
        self.assertEquals(str(llist), str(rev_llist))

    def test_reverse_list_rec_one(self):
        llist = LinkedList()
        rev_llist = reverse_list.reverse_list(llist, use_recursion=True)
        self.assertEquals(str(llist), str(rev_llist))

    def test_reverse_list_iter_even(self):
        llist = list_utils.populate_list(randrange(2, 20, 2))
        llist_str = str(llist)
        rev_llist = reverse_list.reverse_list(llist, use_recursion=False)
        self.assertEquals(llist_str, str(rev_llist)[-1::-1])

    def test_reverse_list_rec_odd(self):
        llist = list_utils.populate_list(randrange(1, 19, 2))
        llist_str = str(llist)
        rev_llist = reverse_list.reverse_list(llist, use_recursion=True)
        self.assertEquals(llist_str, str(rev_llist)[-1::-1])
