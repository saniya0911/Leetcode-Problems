class Solution {
    public String mergeAlternately(String word1, String word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        String ans = "";
        int i = 0;
        while(i < n1 && i < n2)
        {
            ans += word1.charAt(i);
            ans += word2.charAt(i);
            i++;
        }
        while(i < n1)
        {
            ans += word1.charAt(i);
            i++;
        }
        while(i < n2)
        {
            ans += word2.charAt(i);
            i++;
        }
        return ans;
    }
}