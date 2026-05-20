# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append((float('-inf'), root, float('inf')))

        while(q):
            node = q.popleft()
            if node[1]:
                if not node[0] < node[1].val < node[2]:
                    return False
                if node[1].left:
                    q.append((node[0],node[1].left, node[1].val))
                if node[1].right:
                    q.append((node[1].val,node[1].right,node[2]))
        return True