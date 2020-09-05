# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=deque([])
        list2=deque([])

        def dfs_nr(node, l):
            stack = deque([node])
            while stack:
                if stack[-1].left:
                    stack.append(stack[-1].left)
                    continue
                tmp = stack.pop()
                if stack:
                    stack[-1].left = None
                l.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)

        if root1:
            dfs_nr(root1, list1)

        if root2:
            dfs_nr(root2, list2)

        list1.extend(list2)
        return sorted(list1)
