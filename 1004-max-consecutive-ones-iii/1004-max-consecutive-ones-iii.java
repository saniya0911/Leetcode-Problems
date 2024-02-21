class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int max = Integer.MIN_VALUE;
        /*int x=k;
        for(int i =0;i<n;i++)
        {
            int curr = 0;
            int j =i;
            while(j<n && (nums[j]==1 || k!=0))
            {
                curr++;
                if(j<n && nums[j]==0)
                k--;
                j++;
            }
            if(curr>max)
            max = curr;
            k=x;
        }*/
        int zero = 0;
        int curr=0;
        int start=0;
        for(int i = 0;i<n;i++)
        {
            if(nums[i]==0)
            {
                zero++;
            }
            while(zero>k)
            {
                if(nums[start]==0)
                zero--;
                start++;
            }
            curr = i-start+1;
            if(curr>max)
            max=curr;
        }
        return max;
    }
}