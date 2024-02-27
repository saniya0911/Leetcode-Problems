class Solution {
    public String predictPartyVictory(String senate) {
        int n = senate.length();
        Queue<Integer> qr = new LinkedList<>();
        Queue<Integer> qd = new LinkedList<>();
        for(int i =0;i<n;i++)
        {
            if(senate.charAt(i)=='R')
            qr.add(i);
            else
            qd.add(i);
        }
        while(!qr.isEmpty() && !qd.isEmpty())
        {
            int r=qr.poll();
            int d=qd.poll();
            if(r<d)
            qr.add(r+n);
            else
            qd.add(d+n);
        }
        return qr.size()==0?"Dire":"Radiant";
    }
}