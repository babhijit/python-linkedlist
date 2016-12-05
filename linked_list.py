
"""
Node: unit used by linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
LinkedList: Singly Linked List implementation in Python
"""
class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node
        self.current = self.head

    def size(self):
        return self.__size(self.head)

    def clear(self):
        self.head = None
        self.current = None

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def sort(self):
        values = sorted(self.to_list())
        self.clear()
        for value in values:
            self.push(value)

    def clone(self):
        values = self.to_list()
        cloned_list = LinkedList()
        for value in values:
            cloned_list.push(value)
        return cloned_list

    def __size(self, node):
        if not node:
            return 0
        else:
            return 1 + self.__size(node.next)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values += str(current.data)
            current = current.next
        return ' '.join(values)

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(1, 10):
        llist.push(i)
    print('The number of nodes', llist.size())
    print('String representation of the list', str(llist))
