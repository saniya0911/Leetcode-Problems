class Solution {
    public int findJudge(int n, int[][] trust) {
        int size = trust.length;
        int trusting[]=new int[n+1];
        int trusted[]=new int[n+1];
        for(int i =0;i<size;i++)
        {
            int a = trust[i][0];
            int b = trust[i][1];
            trusting[b]+=1;
            trusted[a]+=1;
        }
        for(int i =1;i<=n;i++)
        {
            if(trusting[i]==n-1 && trusted[i]==0)
            return i;
        }
        return -1;
    }
}