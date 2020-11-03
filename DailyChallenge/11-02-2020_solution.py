# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        sorted_list = []
        sorted_nodes = []

        head
        while head != None:
            i = bisect.bisect_left(sorted_list, head.val)
            # print(i)
            sorted_list.insert(i, head.val)
            sorted_nodes.insert(i, head)
            head = head.next

        for i in range(len(sorted_nodes)-1):
            sorted_nodes[i].next = sorted_nodes[i+1]
        sorted_nodes[-1].next = None
        return sorted_nodes[0]
