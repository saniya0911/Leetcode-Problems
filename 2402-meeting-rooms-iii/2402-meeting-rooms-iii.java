class Solution {
    public int mostBooked(int n, int[][] meetings) {
        int k = meetings.length;
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0],b[0]));
        PriorityQueue<Integer> free = new PriorityQueue<>();
        PriorityQueue<Node> end = new PriorityQueue<Node>((a, b) ->(a.end_time!=b.end_time) ?Long.compare(a.end_time,b.end_time) :Long.compare(a.room,b.room));
        int room_used[] = new int[n];
        for(int i = 0;i<n;i++)
        {
            free.add(i);
        }
        for(int i =0;i<k;i++)
        {
            ArrayList<Integer> list = isfree(end,meetings[i][0]);
            if(!list.isEmpty())
            {
                free.addAll(list);
            }
            if(!free.isEmpty())
            {
                room_used[free.peek()]+=1;
                Node temp = new Node(meetings[i][1],free.poll());
                end.add(temp);
                //free.poll();
            }
            else
            {
                Node temp = end.poll();
                int r=temp.room;
                long e = temp.end_time;
                room_used[r]+=1;
                //end.poll();
                temp = new Node(e+(meetings[i][1]-meetings[i][0]),r);
                end.add(temp);
            }
            
        }
        int max = Integer.MIN_VALUE;
        int r = -1;
        for(int i =0;i<n;i++)
        {
            if(room_used[i] > max)
            {
                max = room_used[i];
                r = i;
            }
        }
        return r;
    }
    ArrayList<Integer> isfree(PriorityQueue<Node> end,int start_time)
    {
        int i = end.size();
        ArrayList<Integer> r =new ArrayList<>();
        for(int j=0;j<i;j++)
        {
            if(end.peek().end_time<=start_time)
            {
                Node temp = end.poll();
                r.add(temp.room);
            }
        }
        return r;
    }
}
class Node {
    long end_time;
    int room;
    Node(long e, int r)
    {
        end_time = e;
        room = r;
    }
}