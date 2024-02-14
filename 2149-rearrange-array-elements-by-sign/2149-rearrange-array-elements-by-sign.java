class Solution {
    public int[] rearrangeArray(int[] nums) {
        int l=nums.length;
        int ans[]=new int[l];
        Queue<Integer> neg=new LinkedList<>();
        Queue<Integer> pos=new LinkedList<>();
        for(int i=0;i<l;i++)
        {
            if(nums[i]<0)
                neg.add(nums[i]);
            else
                pos.add(nums[i]);
        }
        for(int i=0;i<l;i++)
        {
            if(i%2==0)
                ans[i]=pos.poll();
            else
                ans[i]=neg.poll();
        }
        return ans;
    }
}