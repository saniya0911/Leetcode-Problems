class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length;
        int dp[]=new int[n+1];
        dp[0]=0;
        for(int i =0;i<n;i++)
        dp[i+1]=dp[i]+gain[i];
        Arrays.sort(dp);
        return dp[n];
    }
}