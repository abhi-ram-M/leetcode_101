# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return 0
            l_h = dfs(root.left)
            r_h = dfs(root.right)
            self.diameter = max(self.diameter, l_h+r_h)
            return 1+max(l_h,r_h)
        dfs(root)
        return self.diameter
        