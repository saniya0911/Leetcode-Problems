class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        if(n<=1)
            return s;
        String maxstr = s.substring(0,1);
        int max = 1;
        
        for(int i = 0; i<n-1; i++)
        {
            String odd = expand(s, i ,i );
            String even = expand(s, i , i+1);
            if(odd.length() > max)
            {
                max = odd.length();
                maxstr = odd;
            }
            if(even.length() > max)
            {
                max = even.length();
                maxstr = even;
            }

        }
        return maxstr;
    }
    String expand(String s, int left, int right)
    {
        while(left>=0 && right < s.length() && s.charAt(left) == s.charAt(right))
        {
            left--;
            right++;
        }
        return s.substring(left+1, right);
    }
}