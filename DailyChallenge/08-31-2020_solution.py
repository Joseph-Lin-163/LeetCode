# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def find_node(self, root, key):
        node = root
        if not node:
            return False

        while True:
            if node.val == key:
                return True
            elif node.left != None and key < node.val:
                node = node.left
            elif node.right != None and key > node.val:
                node = node.right
            else:
                return False

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not self.find_node(root, key):
            return root


        node_prev = TreeNode(right=root)
        to_ret = root
        node = root

        while True:
            if node.val == key:
                # delete this by finding the successor
                # successor is smallest element in right tree
                if node.right:
                    node_follower = node
                    node = node.right


                    found_smallest = False
                    while not found_smallest:
                        if not node.left:
                            found_smallest = True
                            break
                        else:
                            node_follower = node
                            node = node.left

                    # print("node_follower: {}, node: {}, node_prev: {}".format(node_follower.val, node.val, node_prev.val))

                    if node_follower.right == node and node.right:
                        node_follower.right = node.right
                    elif node_follower.right == node and not node.right:
                        node_follower.right = None
                    elif node_follower.left == node and node.right:
                        node_follower.left = node.right
                    else:
                        node_follower.left = None

                    if node_prev.left and node_prev.left.val == key:
                        node_prev.left.val = node.val
                    elif node_prev.right and node_prev.right.val == key:
                        node_prev.right.val = node.val

                    break

                elif node.left:
                    if node_prev.left and node_prev.left.val == key:
                        node_prev.left = node.left
                    elif node_prev.right and node_prev.right.val == key:
                        if node_prev.right == root:
                            node_prev.right = node.left
                            return node_prev.right
                        node_prev.right = node.left
                    break
                else:
                    if node_prev.left and node_prev.left.val == key:
                        node_prev.left = None
                    elif node_prev.right and node_prev.right.val == key:
                        if node_prev.right == root:
                            return None
                        node_prev.right = None
                    break
            elif node.val < key:
                node_prev = node
                node = node.right
            else:
                node_prev = node
                node = node.left


        return root
