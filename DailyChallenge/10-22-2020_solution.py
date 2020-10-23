# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Commented out solution is clean, but hard to tell performance difference in leetcode
        # if not root: return 0
        # queue = [root]
        # level = 1
        # while queue:
        #     next_queue = []
        #     for node in queue:
        #         if not node.left and not node.right:
        #             return level
        #         if node.left:
        #             next_queue.append(node.left)
        #         if node.right:
        #             next_queue.append(node.right)
        #     queue = next_queue
        #     level += 1
        # return level


        if not root:
            return 0

        cnt = 0
        queue = deque([(root,cnt)])

        while queue:
            n = queue.popleft()
            cnt = n[1] + 1
            n = n[0]

            if not n.left and not n.right:
                return cnt
            else:
                if n.left:
                    queue.append((n.left, cnt))
                if n.right:
                    queue.append((n.right, cnt))

        return -1
