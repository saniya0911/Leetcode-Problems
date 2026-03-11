class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int l = 0;
        for(int i = 0; i< s.length(); i++)
        {
            if(s.charAt(i)== ' ')
            {
                l = 0;
                continue;
            }
            l++;
        }
        return l;
    }
}