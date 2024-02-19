class Solution {
    public int compress(char[] chars) {
        String s ="";
        int n = chars.length;
        int k =0;
        for(int i =0;i<n;i++)
        {
            char ch = chars[i];
            s+=ch;
            int x=1;
            while(i<n-1 && chars[i+1]==ch)
            {
                i++;
                x++;
            }
            if(x>1)
            {
                s=s+Integer.toString(x);
            }
        }
        k=s.length();
        for(int i=0;i < k;i++)
        {
            chars[i] = s.charAt(i);
        }
        return k;
    }
}