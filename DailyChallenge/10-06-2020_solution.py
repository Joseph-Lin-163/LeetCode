# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        n = root
        while True:
            if n.val < val and n.right:
                n = n.right
            elif n.val > val and n.left:
                n = n.left
            elif n.val < val and not n.right:
                n.right = TreeNode(val)
                return root
            else:
                n.left = TreeNode(val)
                return root

        # if root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)
        # else:
        #     root.left = self.insertIntoBST(root.left, val)
        # return root
