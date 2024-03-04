class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        Arrays.sort(tokens);
        int n = tokens.length;
        int score=0;
        int max_score=0;
        int left=0;
        int right=n-1;
        while(left<=right)
        {
            if(power>=tokens[left])
            {
                power-=tokens[left];
                score++;
                left++;
                max_score=Math.max(score,max_score);
            }
            else if(score>0)
            {
                power+=tokens[right];
                score--;
                right--;
            }
            else
            break;
        }
        return max_score;
    }
}