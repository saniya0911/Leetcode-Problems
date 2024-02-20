class Solution {
    public boolean isSubsequence(String s, String t) {
        int i =0;
        int l =0;
        for(int j=0;j<t.length();j++)
        {
            if(i==s.length())
            break;
            else if(t.charAt(j)==s.charAt(i))
            {
                l++;
                i++;
            }
        }
        return l==s.length();
    }
}