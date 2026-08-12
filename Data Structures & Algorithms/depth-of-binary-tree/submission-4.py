# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        cnt=0
        while q:
            for i in range(len(q)):
                n=q.popleft()
                if not n:
                    continue
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            cnt+=1
        return cnt