# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        self.dfs(inorder, root)
        return inorder[k-1]
    def dfs(self, inorder, root):
        if not root:
            return
        self.dfs(inorder, root.left)
        inorder.append(root.val)
        self.dfs(inorder, root.right)