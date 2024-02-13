class Solution {
    public String firstPalindrome(String[] words) {
        String ans="";
        for(int i=0;i<words.length;i++)
        {
            StringBuilder s = new StringBuilder(words[i]);
            StringBuilder rev= (new StringBuilder(words[i])).reverse();
            //s.reverse();
            if(words[i].equalsIgnoreCase(rev.toString()))
            {
                ans=rev.toString();
                break;
            }
            
        }
        return ans;
    }
}