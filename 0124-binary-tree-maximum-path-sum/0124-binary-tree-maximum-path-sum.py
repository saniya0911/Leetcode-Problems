# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_value = -inf
        self.dfs(root)
        return self.max_value
    
    def dfs(self, root):
        if not root:
            return 0

        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        self.max_value = max(self.max_value, left + right + root.val)
        return root.val + max(left, right)