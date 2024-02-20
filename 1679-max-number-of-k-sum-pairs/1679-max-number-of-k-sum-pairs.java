class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int f =0;
        int l =n-1;
        int ans =0;
        while(f<l)
        {
            if(nums[f]+nums[l]==k)
            {
                ans++;
                f++;
                l--;
            }
            else if(nums[f]+nums[l]<k)
            f++;
            else
            l--;
        }
        return ans;
    }
}