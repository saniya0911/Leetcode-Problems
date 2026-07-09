class Solution {
    public String reverseVowels(String s) {
        // ArrayList<Character> vowels = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        // String vow = "";
        // String ans = "";
        // int n = s.length();
        // for(int i = 0; i<n ;i++)
        // {
        //     char ch = s.charAt(i);
        //     if(vowels.contains(Character.toLowerCase(ch)))
        //     {
        //         vow += ch;
        //     }
        // }
        // int j = vow.length() -1;
        // for(int i =0 ;i< n;i++)
        // {
        //     char ch = s.charAt(i);
        //     if(vowels.contains(Character.toLowerCase(ch)) && j>=0)
        //     {
        //         ans += vow.charAt(j);
        //         j--;
        //     }
        //     else
        //     {
        //         ans += ch;
        //     }
        // }
        // return ans;
        char ch[] = s.toCharArray();
        String vow= "aeiouAEIOU";
        int low = 0;
        int high = s.length() -1;
        while(low < high)
        {
            while(low < high && vow.indexOf(ch[low]) == -1)
            {
                low++;
            }
            while(low < high && vow.indexOf(ch[high]) == -1)
            {
                high--;
            }
            char temp = ch[low];
            ch[low] = ch[high];
            ch[high] = temp;
            low ++;
            high --;
        }
        String ans = new String(ch);
        return ans;
    }
}