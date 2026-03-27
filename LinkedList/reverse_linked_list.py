# prev -> Nó anterior
# curr -> Nó atual
# next_step -> Guarda o próximo antes de perder a referência

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_step = curr.next
            curr.next = prev
            prev = curr
            curr = next_step

        return prev

## TEST 01
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Print da lista original: 1, 2, 3, 4, 5
head = ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(5)))))
print('1, 2, 3, 4, 5')

sol = Solution()
new_head = sol.reverseList(head)

# Print da lista invertida
result = []
curr = new_head

while curr:
    result.append(str(curr.val))
    curr = curr.next

print(', '.join(result))

## TEST 02
# Print da lista original: 1, 1, 2, 3, 4, 4, 5
head = ListNode(1,
        ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(4,
        ListNode(5)))))))
print('1, 1, 2, 3, 4, 4, 5')

sol = Solution()
new_head = sol.reverseList(head)

result = []
curr = new_head

while curr:
    result.append(str(curr.val))
    curr = curr.next

print(', '.join(result))