# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head == None or head.next == None:
            return head

        length = 1
        h = head
        while h.next != None:
            length += 1
            h = h.next
        tail = h

        if k >= length:
            k = k % length
        if k == 0:
            return head

        length -= k

        h = head
        while length != 1:
            h = h.next
            length -= 1

        ret = h.next
        h.next = None
        tail.next = head

        return ret
