class Solution {
    public String reverseVowels(String s) {
        String upper = "AEIOU";
        String lower = "aeiou";
        StringBuilder vowels=new StringBuilder();
        int n = s.length();
        for(int i=0;i<n;i++)
        {
            char ch=s.charAt(i);
            if(upper.indexOf(ch)==-1 && lower.indexOf(ch)==-1)
                continue;
            else
                vowels.append(ch);
        }
        vowels.reverse();
        int k =0;
        for(int i=0;i<n;i++)
        {
            char ch=s.charAt(i);
            if(upper.indexOf(ch)==-1 && lower.indexOf(ch)==-1)
                continue;
            else
                s=s.substring(0,i)+vowels.charAt(k++)+s.substring(i+1,n);
        }
        return s;
    }
}