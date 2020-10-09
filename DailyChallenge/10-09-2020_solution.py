# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    rt = []
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # Cheeky method is commented out
        # self.rt.append(root)
        # return ""
        if not root:
            return "N"

        left = "L" + self.serialize(root.left)
        right = "R" + self.serialize(root.right)

        return "{}{}{}".format(root.val, left, right)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # return self.rt.pop()
        def helper(data):
            if data[0] == "N":
                return (None, data)

            count = 1
            length = len(data)
            while count < length and (data[count] != "R" and data[count] != "L"):
                count += 1

            t = TreeNode(data[:count])
            if data[count] == 'L':
                t.left, data = helper(data[count + 1:])

            count = 1
            while count < length and (data[count] != "R" and data[count] != "L"):
                count += 1

            if data[count] == 'R':
                t.right, data = helper(data[count + 1:])

            return t, data

        return helper(data)[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
