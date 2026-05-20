"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        hashGraph = {}
        q = collections.deque()
        q.append(node)
        while q:
            nodeTemp = q.popleft()
            if nodeTemp not in hashGraph:
                copy = Node(nodeTemp.val)
                hashGraph[nodeTemp] = copy
            for i in range(len(nodeTemp.neighbors)):
                if nodeTemp.neighbors[i] not in hashGraph:
                    hashGraph[nodeTemp.neighbors[i]] = Node(nodeTemp.neighbors[i].val)
                    q.append(nodeTemp.neighbors[i])
                hashGraph[nodeTemp].neighbors.append(hashGraph[nodeTemp.neighbors[i]])
        return hashGraph[node]
