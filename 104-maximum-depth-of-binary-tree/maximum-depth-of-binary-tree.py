# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            queue = deque([])
            h = 0
            queue.append(root)
            while len(queue) != 0:
                l_s = len(queue)
                h += 1
                for k in range(l_s):
                    e = queue.popleft()
                    if e.left is not None:
                        queue.append(e.left)
                    if e.right is not None:
                        queue.append(e.right)
            return h
        else:
            return 0