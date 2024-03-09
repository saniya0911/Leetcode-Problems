class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int i=0;
        int j=0;
        int n1=nums1.length;
        int n2=nums2.length;
        while(i<n1 && j<n2)
        {
            if(nums1[i]<nums2[j])
            i++;
            else if(nums1[i]>nums2[j])
            j++;
            else
            return nums1[i];
        }
        return -1;
    }
}