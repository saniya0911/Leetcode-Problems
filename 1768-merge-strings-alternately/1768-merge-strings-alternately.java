class Solution {
    public String mergeAlternately(String word1, String word2) {
        String word="";
        int n = word1.length();
        int m = word2.length();
        int i;
        for(i=0; i<n && i<m;i++)
        {
            word=word+word1.charAt(i);
            word=word+word2.charAt(i);
        }
        if(i<n)
        word+=word1.substring(i,n);
        if(i<m)
        word+=word2.substring(i,m);
        return word;
    }
}