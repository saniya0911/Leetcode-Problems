class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        
        ArrayList<int[]> columns = new ArrayList<int[]>();
        for(int i =0;i<n;i++)
        {
            int tempc[]=new int[n];
            for(int j =0;j<n;j++)
            {
                tempc[j]=grid[j][i];
            }
            columns.add(tempc);
        }
        int count=0;
        for(int[] arr:grid)
        {
            for(int[] y:columns)
            {
                if(Arrays.equals(arr,y))
                count++;
            }
        }
        return count;
    }
}