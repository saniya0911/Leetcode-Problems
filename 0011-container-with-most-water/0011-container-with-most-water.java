class Solution {
    public int maxArea(int[] height) {
        int max=Integer.MIN_VALUE;
        int curr_max=0;
        int i=0;
        int n = height.length;
        int j= n-1;
        while(i<j)
        {
            curr_max = (j-i)*Math.min(height[i],height[j]);
            if(curr_max > max)
            max = curr_max;
            if(height[i]<height[j])
            i++;
            else
            j--;
        }
        return max;
    }
}