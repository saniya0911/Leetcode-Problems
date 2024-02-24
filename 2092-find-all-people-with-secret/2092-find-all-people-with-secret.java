class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        //Arrays.sort(meetings,(a,b)->Integer.compare(a[2],b[2]));
        ArrayList<ArrayList<Node>> adj = new ArrayList<>();

        for(int i=0;i<n;i++)
        adj.add(new ArrayList<>());

        for(int[] i:meetings)
        {
            adj.get(i[0]).add(new Node(i[1],i[2]));
            adj.get(i[1]).add(new Node(i[0],i[2]));
        }
        adj.get(0).add(new Node(firstPerson,0));
        Set<Integer> st = new HashSet<>();
        PriorityQueue<Node> q = new PriorityQueue<Node>((a,b)->Integer.compare(a.time,b.time));
        q.add(new Node(0,0));
        while(q.size()>0)
        {
            Node node = q.poll();
            int person = node.person;
            int time = node.time;
            if(st.contains(person))
            continue;

            st.add(person);
            for(Node i: adj.get(person))
            {
                if(i.time>=time && !st.contains(i.person))
                q.add(new Node(i.person,i.time));
            }
        }
        List<Integer> ans = new ArrayList<>(st);
        //for(int i:st)
        //ans.add(i);
        //Collections.sort(ans);
        return ans;
    }
}
class Node
{
    int person;
    int time;
    Node(int p,int t)
    {
        person =p;
        time = t;
    }
}