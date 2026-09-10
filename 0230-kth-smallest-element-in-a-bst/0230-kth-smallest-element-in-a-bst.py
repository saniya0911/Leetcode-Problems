# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return root
        self.ans = 0
        self.count = 0
        self.dfs(root, k)
        return self.ans
    
    def dfs(self, root, k):
        if not root:
            return
        self.dfs(root.left, k)
        self.count += 1
        if self.count == k:
            self.ans = root.val
            return
        if self.count < k:
            self.dfs(root.right, k)

    #     inorder = []
    #     self.dfs(inorder, root)
    #     return inorder[k-1]
    # def dfs(self, inorder, root):
    #     if not root:
    #         return
    #     self.dfs(inorder, root.left)
    #     inorder.append(root.val)
    #     self.dfs(inorder, root.right)