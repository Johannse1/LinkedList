class ListNode:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self,data):
        new_node = ListNode(data=data)
        new_node.next = self.head
        self.head = new_node



