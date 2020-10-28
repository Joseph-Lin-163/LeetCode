# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Not memory O(1)
        visited = set()
        tail = head
        while tail:
            if tail.next in visited:
                return tail.next
            visited.add(tail)
            tail = tail.next
        return None

#       Memory O(1)
#         if not head or head.next == None:
#             return None

#         node = head
#         fast_node = head.next
#         start = head

#         while node != fast_node and fast_node.next != None and fast_node.next.next != None:
#             node = node.next
#             fast_node = fast_node.next.next

#         if fast_node.next == None or fast_node.next.next == None:
#             return None

#         fast_node = fast_node.next
#         node = start

#         while node != fast_node:
#             node = node.next
#             fast_node = fast_node.next

#         return node
