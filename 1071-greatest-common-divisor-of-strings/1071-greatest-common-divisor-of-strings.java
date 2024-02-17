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
        if(b==0)
            return a;
        return gcd(b,a%b);
    }
}