/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null)
        return true;

        else if(p==null || q==null)
        return false;
        
        if(p.val!=q.val)
        return false;
        
        if(p.left==null && q.left==null && p.right==null && q.right==null) 
        {
            if(p.val==q.val)
                return true;
            else
                return false;
        }
        boolean left=false;
        boolean right = false;
        left = isSameTree(p.left,q.left);
        right = isSameTree(p.right,q.right);
        
        return left && right;
    }
}