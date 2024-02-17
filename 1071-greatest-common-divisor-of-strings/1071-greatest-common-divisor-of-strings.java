class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        String prefix="";
        if(!(str1+str2).equalsIgnoreCase(str2+str1))
            return prefix;
        
        int l = gcd(n,m);
        return str1.substring(0,l);
    }
    int gcd(int a,int b)
    {
        int g =1;
        for(int i =1;i<=Math.min(a,b);i++)
        {
            if(a%i==0 && b%i==0)
                g = Math.max(g,i);
        }
        return g;
    }
}