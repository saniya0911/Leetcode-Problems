class Solution {
    public boolean closeStrings(String word1, String word2) {
        int n1 = word1.length();
        int n2= word2.length();
        if(word1.equalsIgnoreCase(word2))
            return true;
        if(n1!=n2)
        return false;

        int fre1[]= new int[26];
        int fre2[]= new int[26];

        for(int i =0;i<n1;i++)
        {
            fre1[word1.charAt(i)-97]+=1;
            fre2[word2.charAt(i)-97]+=1;
        }
        for(int i =0;i<26;i++)
        {
            if((fre1[i]==0 && fre2[i]!=0)||(fre1[i]!=0 && fre2[i]==0))
            return false;
        }
        Arrays.sort(fre1);
        Arrays.sort(fre2);
        for(int i =25;i>=0;i--)
        {
            if(fre1[i]!=fre2[i])
            return false;
        }
        return true;
    }
}