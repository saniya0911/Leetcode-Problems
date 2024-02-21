class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();
        List<Integer> ans2 = new ArrayList<>();
        for(int i =0;i<nums1.length;i++)
        set1.add(nums1[i]);
        for(int j =0;j<nums2.length;j++)
        {
            set2.add(nums2[j]);
            if(!set1.contains(nums2[j]))
            {
                ans2.add(nums2[j]);
                set1.add(nums2[j]);
            }
        }

        List<Integer> ans1 = new ArrayList<>();
        for(int i =0;i<nums1.length;i++)
        {
            if(!set2.contains(nums1[i]))
            {
                ans1.add(nums1[i]);
                set2.add(nums1[i]);
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(ans1);
        ans.add(ans2);
        return ans;
    }
}