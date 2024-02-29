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
    public boolean isEvenOddTree(TreeNode root) {
        if(root==null)
        return false;

        if(root.val%2==0)
        return false;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int level=0;
        while(!q.isEmpty())
        {
            int l = q.size();
            int min=Integer.MIN_VALUE;
            int max = Integer.MAX_VALUE;
            for(int  i=0;i<l;i++)
            {
                TreeNode n=q.poll();
                int node = n.val;
                if(n.left!=null)
                q.add(n.left);
                if(n.right!=null)
                q.add(n.right);

                if(level%2==0)
                {
                if(node%2==0 || node<=min)
                return false;
                else
                min=node;
                }
                else
                {
                    if(node%2!=0 || node>=max)
                    return false;
                    else
                    max=node;
                }
            }
            level++;
        }
        return true;
    }
}