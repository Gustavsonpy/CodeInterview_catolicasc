class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
        self.length += 1

    def show_all_nodes(self):
        aux = self.head
        count = 1
        while aux:
            print(f'Node {count}: {aux.value}')
            aux = aux.next
            count += 1

    def swap_nodes(self):
        if not self.head or not self.head.next:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        self.head = dummy.next


# ===== Teste =====
exList = ListNode()
exList.append(1)
exList.append(2)
exList.append(3)
exList.append(4)

print("Antes:")
exList.show_all_nodes()

exList.swap_nodes()

print("\nDepois:")
exList.show_all_nodes()