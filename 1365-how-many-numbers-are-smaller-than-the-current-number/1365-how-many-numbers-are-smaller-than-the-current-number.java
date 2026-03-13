class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int count[] = new int[101];
        int ans[] = new int[nums.length];
        
        for(int i = 0; i<nums.length; i++)
        {
            count[nums[i]]++;
        }

        for(int i = 1;i<=100; i++)
        {
            count[i] += count[i-1];
        }

        for(int i = 0; i< nums.length; i++)
        {
            if(nums[i] ==0)
                ans[i] = 0;
            else
                ans[i] = count[nums[i] - 1];
        }


        // for(int i =0; i< nums.length; i++)
        // {
        //     int count = 0;
        //     for(int j = 0; j< nums.length; j++)
        //     {
        //         if(i!=j && nums[j]<nums[i])
        //             count++;
        //     }
        //     ans[i] = count;
        // }
        return ans;
    }
}