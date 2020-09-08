# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        sum_total = 0
        stack = deque([root])
        while stack:
            if stack[-1].left and stack[-1].left != -1:
                stack.append(stack[-1].left)
                continue
            if stack[-1].right and stack[-1].right != -1:
                stack.append(stack[-1].right)
                continue

            # Reached a leaf
            if stack[-1].left == None and stack[-1].right == None:
                sum_total += int("".join([str(x.val) for x in stack]), 2)
            tmp = stack.pop()

            if stack:
                if stack[-1].left == tmp:
                    stack[-1].left = -1
                else:
                    stack[-1].right = -1

        return sum_total
