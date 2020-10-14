# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def printlist():
            htmp = head
            while htmp != None:
                print(htmp.val, end=" ")
                htmp = htmp.next
            print("")

        if not head or head.next == None:
            return head

        length = 1
        n = head
        while n.next != None:
            n = n.next
            length += 1

        ws = 2
        while ws < length*2:
            iters = math.ceil(length/ws)
            n = head
            for it in range(iters):
                if not n or n.next == None:
                        continue

                n_fast = n
                n_end = n
                n_stop = n
                half_ws = ws//2
                ws_bk = ws
                if it == iters-1:
                    len_it = 1
                    n_tmp = n
                    while n_tmp.next != None:
                        n_tmp = n_tmp.next
                        len_it += 1
                    if half_ws >= len_it:
                        if ws != ws_bk:
                            ws = ws_bk
                        continue
                    else:
                        for j in range(len_it):
                            n_stop = n_stop.next
                            if j < half_ws:
                                n_fast = n_fast.next
                            if j < half_ws - 1:
                                n_end = n_end.next
                        ws = len_it
                else:
                    for j in range(ws):
                        n_stop = n_stop.next
                        if j < half_ws:
                            n_fast = n_fast.next
                        if j < half_ws - 1:
                            n_end = n_end.next

                # Comparisons
                for j in range(ws):
                    # print("ws: {}, j: {}".format(ws, j))
                    # print("n: {}, n_fast: {}, n_stop: {}, n_end: {}".format(n.val if n else None, n_fast.val if n_fast else None, n_stop.val if n_stop else None, n_end.val if n_end else None))
                    # printlist()
                    if not n_fast or n_fast == n_stop or (n.val <= n_fast.val and n != n_end):
                        n = n.next
                    elif n.val <= n_fast.val and n == n_end:
                        n_fast = n_fast.next
                    elif n.val > n_fast.val:
                        if n.next == n_fast: # n == n_end
                            n_fast.val, n.val = n.val, n_fast.val
                            n_fast = n_fast.next
                            n = n.next
                            n_end = n
                        else:
                            # print("ping")
                            n_end_next = True if n_end.next == n_fast else False
                            tmp = ListNode(n.val)
                            tmp.next = n.next
                            n.val = n_fast.val
                            n.next = tmp
                            n = n.next
                            n_fast = n_fast.next
                            if n_end_next:
                                n_end.next = n_fast

                if ws != ws_bk:
                    ws = ws_bk
                n = n_stop
            ws *= 2




        return head
            # Basically, the idea is to mergesort iteratively
            # To do that, we must assign a fast pointer that starts at half-way of the window size
            # Also have one pointer at the "end" of first half for merging operation
            # Then compare the two pointers to see which is smaller
            # If left pointer is smaller, operation is simple: move slow pointer forwards
            # If the right pointer is smaller, then need to have the pointer at the end of first half
            # point to the next node after the smaller (merging operation)
            # Then, double the window size and repeat
            # TODO: figure out what needs to be done in terms of edge cases (say that LL size is 13)
            # if LL size is 13, we get 2 -> 4 -> 8
            # but on one end, we see that we have 8, on the other, we have 5
            # So we need to deal with that

        
