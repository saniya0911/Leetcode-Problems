# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        n = len(inorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        parent = TreeNode(preorder[0])
        # p = self.parent_index(parent.val, inorder)
        p = inorder.index(parent.val)
        left = self.buildTree(preorder[1:], inorder[0:p])
        right = self.buildTree(preorder[p+1:], inorder[p+1:])
        parent.left = left
        parent.right = right
        return parent

    def parent_index(self, target, nums):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return len(nums) - 1
