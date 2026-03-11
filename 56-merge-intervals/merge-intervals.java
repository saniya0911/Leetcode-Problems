class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        List<int[]> ans = new ArrayList<>();
        for(int in[]:intervals)
        {
            if(ans.isEmpty() || ans.get(ans.size()-1)[1] < in[0])
            {
                ans.add(in);
            }
            else
            {
                ans.get(ans.size()-1)[1] = Math.max(in[1], ans.get(ans.size()-1)[1]);
            }
        }
        return ans.toArray(new int[ans.size()][]);
    }
}