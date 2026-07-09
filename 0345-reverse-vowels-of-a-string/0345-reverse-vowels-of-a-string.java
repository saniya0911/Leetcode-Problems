class Solution {
    public String reverseVowels(String s) {
        ArrayList<Character> vowels = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        String vow = "";
        String ans = "";
        int n = s.length();
        for(int i = 0; i<n ;i++)
        {
            char ch = s.charAt(i);
            if(vowels.contains(Character.toLowerCase(ch)))
            {
                vow += ch;
            }
        }
        int j = vow.length() -1;
        for(int i =0 ;i< n;i++)
        {
            char ch = s.charAt(i);
            if(vowels.contains(Character.toLowerCase(ch)) && j>=0)
            {
                ans += vow.charAt(j);
                j--;
            }
            else
            {
                ans += ch;
            }
        }
        return ans;
    }
}