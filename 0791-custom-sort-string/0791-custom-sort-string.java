class Solution {
    public String customSortString(String order, String s) {
        String ans="";
        int n = order.length();
        HashMap<Character,Integer> map = new HashMap<>();
        for(int i =0;i<s.length();i++)
        {
            char ch = s.charAt(i);
            map.put(ch,map.getOrDefault(ch,0)+1);
        }
        for(int i =0; i <n; i++)
        {
            char ch = order.charAt(i);
            if(map.containsKey(ch))
            {
                char[] repeat = new char[map.get(ch)];
                Arrays.fill(repeat, ch);
                ans += new String(repeat);
                map.remove(ch);
            }
        }
        if(map.size()!=0)
        {
            for(Map.Entry<Character,Integer> e: map.entrySet())
            {
                char[] repeat = new char[e.getValue()];
                Arrays.fill(repeat, e.getKey());
                ans += new String(repeat);
            }
        }
        return ans;
    }
}