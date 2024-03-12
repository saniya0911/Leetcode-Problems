/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode node=new ListNode(0);
        node.next=head;

        int presum=0;
        HashMap<Integer,ListNode> map = new HashMap<>();
        ListNode current=node;
        while(current!=null)
        {
            presum+=current.val;
            if(map.containsKey(presum))
            {
                ListNode pre=map.get(presum);
                ListNode temp = pre.next;
                int p = presum+(temp != null?temp.val:0);

                while(p!=presum)
                {
                    map.remove(p);
                    temp=temp.next;
                    p+=(temp!=null?temp.val:0);
                }
                pre.next=current.next;
            }
            else
            {
                map.put(presum,current);
            }
            current=current.next;
        }
        return node.next;
    }
}