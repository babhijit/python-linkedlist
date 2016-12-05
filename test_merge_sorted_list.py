from unittest import TestCase
from linked_list import LinkedList
from random import randrange
import list_utils
import merge_sorted_list


class TestMerge_sorted_list(TestCase):
    def test_merge_sorted_ist_empty(self):
        list1 = LinkedList()
        list2 = LinkedList()
        self.assertEquals(list1.size(), 0)
        self.assertEquals(list2.size(), 0)
        merged_list = merge_sorted_list.merge_sorted_list(list1=list1.to_list(), list2=list2.to_list())
        self.assertEquals(len(merged_list), 0)

    def test_merge_sorted_list_list1_empty(self):
        list1 = []
        self.assertEquals(len(list1), 0)
        list2 = list_utils.populate_list(randrange(1, 19, 2)).to_list()
        sorted(list2)
        merged_list = merge_sorted_list.merge_sorted_list(list1=list1, list2=list2)
        self.assertEquals(merged_list, list2)

    def test_merge_sorted_list_list2_empty(self):
        list1 = sorted(list_utils.populate_list(randrange(1, 19, 2)).to_list())
        list2 = []
        self.assertEquals(len(list2), 0)
        merged_list = merge_sorted_list.merge_sorted_list(list1=list1, list2=list2)
        self.assertEquals(merged_list, list1)

    def test_merge_sorted_list(self):
        list1 = sorted(list_utils.populate_list(randrange(1, 19)).to_list())
        list2 = sorted(list_utils.populate_list(randrange(1, 19)).to_list())
        sorted_merged_list = list1[:]
        sorted_merged_list.extend(list2)
        sorted_merged_list = sorted(sorted_merged_list)
        merged_list = merge_sorted_list.merge_sorted_list(list1=list1, list2=list2)
        self.assertEquals(merged_list, sorted_merged_list)

    def test_merge_sorted_list_list1_gt_list2(self):
        list1 = sorted(list_utils.populate_list(randrange(20, 39)).to_list())
        list2 = sorted(list_utils.populate_list(randrange(1, 19)).to_list())
        sorted_merged_list = list1[:]
        sorted_merged_list.extend(list2)
        sorted_merged_list = sorted(sorted_merged_list)
        merged_list = merge_sorted_list.merge_sorted_list(list1=list1, list2=list2)
        self.assertEquals(merged_list, sorted_merged_list)

    def test_merge_sorted_list_list1_lt_list2(self):
        list1 = sorted(list_utils.populate_list(randrange(1, 19)).to_list())
        list2 = sorted(list_utils.populate_list(randrange(20, 39)).to_list())
        sorted_merged_list = list1[:]
        sorted_merged_list.extend(list2)
        sorted_merged_list = sorted(sorted_merged_list)
        merged_list = merge_sorted_list.merge_sorted_list(list1=list1, list2=list2)
        self.assertEquals(merged_list, sorted_merged_list)
