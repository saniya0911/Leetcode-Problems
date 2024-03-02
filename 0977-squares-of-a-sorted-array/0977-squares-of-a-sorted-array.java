class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int ar[]=new int[n];
        for(int i =0;i<n;i++)
        ar[i]=nums[i]*nums[i];

        Arrays.sort(ar);
        return ar;
    }
}