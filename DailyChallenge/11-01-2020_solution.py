# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        while head:
            s += str(head.val)
            head = head.next

        return int(s,2)

#         length = -1
#         node = head
#         while node != None:
#             node = node.next
#             length += 1

#         s = 0
#         while head != None:
#             # print(count, head.val, 1<<count)
#             if head.val == 1:
#                 s |= (1<<length)
#             length -= 1
#             head = head.next

#         return s
