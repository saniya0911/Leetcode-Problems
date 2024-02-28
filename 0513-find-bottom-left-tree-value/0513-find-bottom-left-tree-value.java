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
    HashMap<TreeNode,Integer> h = new HashMap<TreeNode,Integer>();
    public int findBottomLeftValue(TreeNode root) {
        h.put(root,0);
        TreeNode node = solve(root);
        return node.val;
    }
    TreeNode solve(TreeNode root)
    {
        if(root==null)
        return null;

        height(root,root.left);
        height(root,root.right);

        if(root.left == null && root.right == null)
        return root;

        TreeNode left = solve(root.left);
        TreeNode right = solve(root.right);
        int lh=0,rh=0;
        
        if(left!=null)
        lh = h.get(left);
        if(right!=null)
        rh = h.get(right);
        
        return rh>lh?right:left;
    }
    void height(TreeNode root,TreeNode node)
    {
        if(root==null || node==null)
        return;

        h.put(node,h.getOrDefault(root,0)+1);
    }
}