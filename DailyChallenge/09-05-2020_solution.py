# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        d = {}
        q = []
        if root1:
            q.append(root1)
        while q:
            d[q[0].val] = d.get(q[0].val, 0) + 1
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q.pop(0)
        if root2:
            q.append(root2)
        while q:
            d[q[0].val] = d.get(q[0].val, 0) + 1
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q.pop(0)

        return [x for x in sorted(d) for y in range(d[x])]
