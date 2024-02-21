class Solution {
    public int maxVowels(String s, int k) {
        String vowels = "aeiou";
        int curr=0;
        for(int i =0;i<k;i++)
        {
            char ch = s.charAt(i);
            if(vowels.indexOf(ch)!=-1)
            curr++;
        }
        int max = curr;
        int n = s.length();
        for(int i=1;i+k-1<n;i++)
        {
            char ch1=s.charAt(i-1);
            char ch2=s.charAt(i+k-1);
            if(vowels.indexOf(ch1)!=-1)
            curr--;
            if(vowels.indexOf(ch2)!=-1)
            curr++;
            if(curr>max)
            max = curr;
        }
        return max;
    }
}