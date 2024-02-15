class Solution {
    public boolean isValid(String str) {
        Stack<Character> s=new Stack<>();
        for(int i=0;i<str.length();i++)
        {
            char ch=str.charAt(i);
            if(ch=='(' || ch=='{' || ch=='[')
                s.push(ch);
            else if(ch==')' && !s.isEmpty() && s.peek()=='(')
                s.pop();
            else if(ch=='}' && !s.isEmpty() && s.peek()=='{')
                s.pop();
            else if(ch==']' && !s.isEmpty() && s.peek()=='[')
                s.pop();
            else
                return false;
        }
        return s.isEmpty();
    }
}