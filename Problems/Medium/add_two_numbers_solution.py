# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newNode = ListNode()
        node = newNode
        carry = 0
        not_first = False
        while l1 != None or l2 != None or carry != 0:
            tmp_total = 0
            
            if l1:
                tmp_total += l1.val
                l1 = l1.next
            if l2:
                tmp_total += l2.val
                l2 = l2.next
                
            if carry == 1:
                tmp_total += 1
                carry = 0
                
            if tmp_total >= 10:
                tmp_total -= 10
                carry = 1
                
            node.val = tmp_total
            if (l1 != None or l2 != None or carry != 0):
                if (l1 == None or l2 == None) and carry == 0:
                    if l1 == None:
                        node.next = l2
                        return newNode
                    elif l2 == None:
                        node.next = l1
                        return newNode

                node.next = ListNode()
                node = node.next
            
            
            
        return newNode
