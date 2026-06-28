class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.length;
        // int can[] = new int[n];
        // boolean result[] = new boolean[n];
        ArrayList<Boolean> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for(int i = 0; i< n; i++)
        {
            // can[i] = candies[i] + extraCandies;
            if(max<candies[i])
                max = candies[i];
        }
        for(int i = 0; i< n; i++)
        {
            if(candies[i] + extraCandies >= max)
                result.add(true);
            else
                result.add(false);
        }
        return result;
    }
}