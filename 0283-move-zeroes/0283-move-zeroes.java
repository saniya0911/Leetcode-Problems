class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int f =0;
        int z =0;
        int i =0;
        while(i<n)
        {
            if(nums[i]!=0)
            {
                nums[f]=nums[i];
                f++;
            }
            else
            {
                z++;
            }
            i++;
        }
        for(int j =n-z;j<n;j++)
        nums[j]=0;
    }
}