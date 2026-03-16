class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MAX_VALUE;
        int curr = 0;
        int max = 0;

        for(int i = 0; i< prices.length; i++)
        {
            System.out.println("yes");
            buy = Math.min(prices[i], buy);
            curr = prices[i]-buy;
            max = Math.max(max, curr);
        }
        return max;
    }
}