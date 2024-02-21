class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        int zero=0;
        int start=0;
        int max = 0;
        for(int i =0;i<n;i++)
        {
            if(nums[i]==0)
            zero++;
            while(zero>1)
            {
                if(nums[start]==0)
                zero--;
                start++;
            }
            max=Math.max(max,i-start-zero+1);
        }
        if(zero==0)
        max-=1;
        return max;
    }
}