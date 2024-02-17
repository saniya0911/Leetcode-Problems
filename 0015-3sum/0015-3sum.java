class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        HashSet<List<Integer>> set = new HashSet<>();
        for(int i =0 ;i<n; i++)
        {
            int j = i+1;
            int k = n-1;
            while(j<k)
            {
                List<Integer> triplet = new ArrayList<>();
                int s = nums[i] + nums[j] + nums[k];
                if(s==0)
                {
                    triplet.add(nums[i]);
                    triplet.add(nums[j]);
                    triplet.add(nums[k]);
                    set.add(triplet);
                    j++;
                    k--;
                }
                else if (s>0)
                k--;
                else
                j++;
            }
        }
        List<List<Integer>> ans = new ArrayList<>(set);
        return ans;
    }
}