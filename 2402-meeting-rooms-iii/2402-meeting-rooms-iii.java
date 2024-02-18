class Solution {
    public int mostBooked(int n, int[][] meetings) {
        int k = meetings.length;
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0],b[0]));
        int room_used[]=new int[n];
        long free_time[]=new long[n];
        for(int i = 0;i<k;i++)
        {
            int start = meetings[i][0];
            int end = meetings[i][1];
            long min_time = Long.MAX_VALUE;
            int min_room = -1;
            boolean flag = false;
            for(int j =0;j<n;j++)
            {
                if(free_time[j]<=start)
                {
                    room_used[j]++;
                    free_time[j]=end;
                    flag = true;
                    break;
                }
                if(min_time>free_time[j])
                {
                    min_time = free_time[j];
                    min_room = j;
                }
            }
                if(!flag)
                {
                    room_used[min_room]++;
                    free_time[min_room]+=end-start;
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
}