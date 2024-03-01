class Solution {
    public String maximumOddBinaryNumber(String s) {
        Stack<Character> ones = new Stack<>();
        Stack<Character> zeros = new Stack<>();
        int l = s.length();
        for(int i =0;i<l;i++)
        {
            char ch = s.charAt(i);
            if(ch=='1')
            ones.add(ch);
            else
            zeros.add(ch);
        }
        int n = ones.size();
        String ans ="";
        for(int i =1;i<n;i++)
        ans+=ones.pop();
        while(!zeros.isEmpty())
        ans+=zeros.pop();

        ans+=ones.pop();
        return ans;
    }
}