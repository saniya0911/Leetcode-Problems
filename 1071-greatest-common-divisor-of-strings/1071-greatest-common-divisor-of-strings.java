class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        String prefix="";
        int l =0;
        for(int i=0;i<n && i<m;i++)
        {
            if(str1.charAt(i)==str2.charAt(i))
            {
                prefix+=str1.charAt(i);
                l++;
            }
            else
            break;
        }
        for(int i=l;i>0;i--)
        {
            if(gcd(str1,str2,prefix.substring(0,i)))
            return prefix.substring(0,i);
        }
        return "";
    }
    boolean gcd(String str1, String str2, String prefix)
    {
        int n = str1.length();
        int m = str2.length();
        int k = prefix.length();
        String divisor1 = "";
        for(int i =0;i<Math.min(n,m);i+=k)
        {
            divisor1+=prefix;
        }
        String divisor2=divisor1;

        for(int i = Math.min(n,m);i<Math.max(n,m);i+=k)
        divisor2+=prefix;

        if((divisor1.equalsIgnoreCase(str1) || divisor1.equalsIgnoreCase(str2)) && (divisor2.equalsIgnoreCase(str1) || divisor2.equalsIgnoreCase(str2)))
        return true;
        else
        return false;
    }
}