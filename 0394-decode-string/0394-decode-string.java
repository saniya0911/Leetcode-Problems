class Solution {
    public String decodeString(String s) {
        Stack<Integer> dig = new Stack<>();
        Stack<StringBuilder> letter = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int n=0;
        for(char c:s.toCharArray())
        {
            if(Character.isDigit(c))
            {
                n=n*10+(c-'0');
            }
            else if(c=='[')
            {
                dig.add(n);
                n=0;
                letter.add(sb);
                sb = new StringBuilder();
            }
            else if(c==']')
            {
                int i = dig.pop();
                StringBuilder temp = sb;
                sb=letter.pop();
                while(i-->0)
                sb.append(temp);
            }
            else
            sb.append(c);
        }
        return sb.toString();
    }
}