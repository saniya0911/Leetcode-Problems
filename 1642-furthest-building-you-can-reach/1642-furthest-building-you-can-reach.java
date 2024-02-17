class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        //int ans = 0;
        int n = heights.length;
        int i=0;
        PriorityQueue<Integer> jumps = new PriorityQueue<>(Collections.reverseOrder());
        for(i=0;i<n-1;i++)
        {
            int diff = heights[i+1]-heights[i];
            if(diff<=0)
            continue;
            else
            {
                bricks-=diff;
                jumps.add(diff);
                if(bricks<0)
                {
                    bricks+=jumps.poll();
                    if(ladders>0)
                    ladders--;
                    else
                    break;
                }
            }
        }
        return i;
    }
}