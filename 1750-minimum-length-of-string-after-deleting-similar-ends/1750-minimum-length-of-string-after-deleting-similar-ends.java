class Solution {
    public int minimumLength(String s) {
        int n = s.length();
        int f =0;
        int l =n-1;
        int k=0;
        
        while(f<l && s.charAt(f)==s.charAt(l))
        {
            //k++;
            if((f+1)!=l && s.charAt(f+1)==s.charAt(l))
            {
                f++;
                k++;
            }
            else if(f!=(l-1) && s.charAt(f)==s.charAt(l-1))
            {
                l--;
                k++;
            }
            else
            {
                f++;
                l--;
                k+=2;
            }
        }
        return (n-k);
    }
}