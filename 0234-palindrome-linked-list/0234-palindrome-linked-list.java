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
    public boolean isPalindrome(ListNode head) {
        if(head==null || head.next==null)
        return true;

        ListNode front = head;
        ArrayList<Integer> list = new ArrayList<>();
        while(front!=null)
        {
            list.add(front.val);
            front = front.next;
        }
        int n = list.size();
        for(int i =0;i<n/2;i++)
        {
            if(list.get(i)!=list.get(n-i-1))
            return false;
        }
        return true;
    }
}