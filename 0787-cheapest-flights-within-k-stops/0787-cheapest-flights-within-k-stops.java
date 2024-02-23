class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int cost[]=new int[n];
        for(int i =0;i<n;i++)
        cost[i]=Integer.MAX_VALUE;
        cost[src]=0;
        for (int i = 0; i <= k; i++) {
            int[] temp = Arrays.copyOf(cost, n);
            for (int[] flight : flights) {
                if (cost[flight[0]] != Integer.MAX_VALUE) {
                    temp[flight[1]] = Math.min(temp[flight[1]], cost[flight[0]] + flight[2]);
                }
            }
            cost = temp;
        }
        
        return cost[dst] == Integer.MAX_VALUE ? -1 : cost[dst];

    }
}