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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int k =0;
        ListNode node = head;
        while(node.next!=null)
        {
            k++;
            node=node.next;
        }
        n=k-n;
        if(n==-1)
        return head.next;

        node = head;
        while(n>0)
        {
            node=node.next;
            n--;
        }
        node.next=node.next.next;
        return head;
    }
}