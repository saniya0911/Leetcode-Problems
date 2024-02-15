class Solution {
    public int maxSum(int[] nums) {
        //Arrays.sort(nums);
        int ans=-1;
        int n=nums.length;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                int res=nums[i]+nums[j];
                if(maxdigit(nums[i],nums[j]))
                ans=Math.max(res,ans);
            }
        }
        return ans;
    }
    boolean maxdigit(int a,int b)
    {
        int m1=-1;
        int m2=-1;
        while(a>0)
        {
            m1=Math.max(m1,a%10);
            a=a/10;
        }
        while(b>0)
        {
            m2=Math.max(m2,b%10);
            b=b/10;
        }
        if(m1==m2)
        return true;

        return false;
    }
}