"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        if len(node.neighbors) == 0:
            return Node(node.val)

        queue = deque([node])
        access = {node.val: Node(node.val)}

        while queue:
            n = queue.pop()
            for neighbor in n.neighbors:
                if neighbor.val not in access:
                    queue.append(neighbor)
                    access[neighbor.val] = Node(neighbor.val)

                access[n.val].neighbors.append(access[neighbor.val])

        return access[1]
                
