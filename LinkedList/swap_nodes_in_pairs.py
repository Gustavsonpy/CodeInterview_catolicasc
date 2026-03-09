class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

class ListNode:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_no = Node(value)
        if self.head is None:
            self.head = new_no
        else:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = new_no

exList = ListNode()
exList.append(3)