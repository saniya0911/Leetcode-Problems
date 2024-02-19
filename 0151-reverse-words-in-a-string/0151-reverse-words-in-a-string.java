class Solution {
    public String reverseWords(String s) {
        String ans = "";
        String word = "";
        s.trim();
        s=s+" ";
        int n = s.length();
        for(int i =0;i<n;i++)
        {
            char ch = s.charAt(i);
            if(ch!=' ')
            word+=ch;
            else
            {
                ans=" "+word+ans;
                word = "";
                while(i<n && s.charAt(i)==' ')
                i++;
                i--;
            }
        }
        ans = ans.trim();
        return ans;
    }
}