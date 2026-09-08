# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -inf, inf)

    def dfs(self, root, l, r):
        if not root:
            return True
        if root.val <= l or root.val >= r:
            return False
        
        if not root.left and not root.right:
            return True

        if not root.left:
            return root.val < root.right.val and self.dfs(root.right, root.val, r)
        
        if not root.right:
            return root.val > root.left.val and self.dfs(root.left, l, root.val)
        
        if root.val > root.left.val and root.val < root.right.val and self.dfs(root.left, l, root.val) and self.dfs(root.right, root.val, r):
            return True

        return False