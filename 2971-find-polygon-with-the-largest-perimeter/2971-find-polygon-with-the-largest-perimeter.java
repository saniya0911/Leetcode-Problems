class Solution {
    public long largestPerimeter(int[] nums) {
       Arrays.sort(nums);
       int n=nums.length;
       long dp[]=new long[n];
       dp[0]=0;
       for(int i=1;i<n;i++)
       {
           dp[i]=dp[i-1]+nums[i-1];
       }
       //int longest=-1;
       for(int i=n-1;i>=2;i--)
       {
            if(dp[i]>nums[i])
            {
                return dp[i]+nums[i];
            }
       }
       /*int peri=0;
       if(longest!=-1)
       {
           for(int i=0;i<=longest;i++)
           peri+=peri+nums[i];
           return peri;
       }*/
       return -1;
    }
}