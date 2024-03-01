class Solution {
    public String maximumOddBinaryNumber(String s) {
        /*Stack<Character> ones = new Stack<>();
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

        ans+=ones.pop();*/
        
        int ones=0;
        int zeros=0;
        int n = s.length();
        
        for(int i=0;i<n;i++)
        {
            char ch = s.charAt(i);
            if(ch=='1')
                ones++;
            else
                zeros++;
        }
        String ans ="";
        while(ones>1)
        {
            ans+='1';
            ones--;
        }
        while(zeros>0)
        {
            ans+='0';
            zeros--;
        }
        
        ans+='1';
        return ans;
    }
}