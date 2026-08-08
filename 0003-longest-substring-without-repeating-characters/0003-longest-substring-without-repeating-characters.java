class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n==0)
            return 0;
        int curr = 0;
        int max = 0;
        String str = "";
        for(int i =0; i<n;i++)
        {
            char ch = s.charAt(i);
            if(str.indexOf(ch) == -1)
            {
                curr++;
                str = str + ch;
            }
            else
            {
                max = Math.max(max, curr);
                str = str.substring(str.indexOf(ch)+1) + ch;
                curr = str.length();
            }
        }
        return Math.max(max, curr);
    }
}