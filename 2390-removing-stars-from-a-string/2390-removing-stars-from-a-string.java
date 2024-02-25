class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        int n = s.length();
        for(int i =0;i<n;i++)
        {
            char ch=s.charAt(i);
            if(ch!='*')
            stack.add(ch);
            else
            {
                stack.pop();
            }
        }
        String ans="";
        while(!stack.isEmpty())
        ans=stack.pop()+ans;
        return ans;
    }
}