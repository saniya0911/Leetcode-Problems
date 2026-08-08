class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        if (n==0)
            return 0;

        int curr = 1;
        int max = 1;
        
        HashSet<Integer> set = new HashSet<>();
        for(int i =0; i<n ; i++)
            set.add(nums[i]);

        for(int i: set)
        {
            if(!set.contains(i-1))
            {
                int x = i;
                while(set.contains(x+1))
                {
                    curr++;
                    x++;
                }
                max = Math.max(max, curr);
            }
            max = Math.max(max, curr);
            curr = 1;
        }
        return Math.max(max, curr);
    }
}