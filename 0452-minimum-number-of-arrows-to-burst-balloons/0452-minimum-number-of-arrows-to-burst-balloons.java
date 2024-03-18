class Solution {
    public int findMinArrowShots(int[][] points) {
        int count =1;
        Arrays.sort(points,(a,b)->Integer.compare(a[1],b[1]));
        int n = points.length;
        int prev = points[0][1];
        for(int i=0;i<n;i++)
        {
            if(prev<points[i][0])
            {
                count++;
                prev = points[i][1];
            }
        }
        return count++;
    }
}