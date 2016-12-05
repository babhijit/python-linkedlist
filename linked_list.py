
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

    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def size(self):
        return self.__size(self.head)

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
