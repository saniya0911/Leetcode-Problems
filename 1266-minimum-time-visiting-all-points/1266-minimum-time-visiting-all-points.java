class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int time = 0;
        int x0 = points[0][0];
        int y0 = points[0][1];

        for(int i = 1; i< points.length; i++)
        {
            int p[] = points[i];
            int x = p[0];
            int y = p[1];
            time += Math.max(Math.abs(x-x0), Math.abs(y-y0));
            x0 = x; 
            y0 = y;
        }
        return time;
    }
}