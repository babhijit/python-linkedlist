"""
merges two sorted linked lists
"""


def merge_sorted_list(list1 :list, list2: list):
    if list1 is None:
        return list2[:]
    if list2 is None:
        return list1[:]

    merged_list = []
    list1_len = len(list1)
    list2_len = len(list2)

    cidx_1 = 0
    cidx_2 = 0

    while cidx_1 < list1_len and cidx_2 < list2_len:
        if list1[cidx_1] < list2[cidx_2]:
            merged_list.append(list1[cidx_1])
            cidx_1 += 1
        else:
            merged_list.append(list2[cidx_2])
            cidx_2 += 1

    if cidx_1 < list1_len:
        merged_list.extend(list1[cidx_1:])
    else:
        merged_list.extend(list2[cidx_2:])

    return merged_list
