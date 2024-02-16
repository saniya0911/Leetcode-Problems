class Solution {
    public int strStr(String haystack, String needle) {
        int len=needle.length();
        //int ans=-1;
        if(haystack.equalsIgnoreCase(needle))
            return 0;
        for(int i=0;i<=haystack.length()-len;i++)
        {
            if(haystack.substring(i,i+len).startsWith(needle))
            return i;
        }
        return -1;
    }
}