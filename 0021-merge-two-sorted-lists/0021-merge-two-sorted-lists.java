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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list = new ListNode();
        /*ListNode head1=list1;
        ListNode head2=list2;
        int l1=0;
        int l2=0;
        while(head1!=null)
        {
            l1++;
            head1=head1.next;
        }
        while(head2!=null)
        {
            l2++;
            head2=head2.next;
        }
        int i=0,j=0;*/
        ListNode temp=new ListNode();
        if(list1!=null && list2!=null && list1.val<list2.val)
        {
            temp.val = list1.val;
            list1=list1.next;
            //i++;
        }
        else if (list1!=null && list2!=null && list1.val>=list2.val)
        {
            temp.val = list2.val;
            list2=list2.next;
            //j++;
        }
        else if(list1!=null)
        {
            temp.val = list1.val;
            list1=list1.next;
            //i++;
        }
        else if(list2!=null)
        {
            temp.val = list2.val;
            list2=list2.next;
            //j++;
        }
        else
        return list.next;

        list = temp;
        while(list1!=null && list2!=null)
        {
            ListNode head=new ListNode();
            if(list1.val<list2.val)
            {
                head.val=list1.val;
                list1=list1.next;
            }
            else
            {
                head.val=list2.val;
                list2=list2.next;
            }
            temp.next=head;
            temp=temp.next;
        }
        while(list1!=null)
        {
            ListNode head=new ListNode();
            head.val=list1.val;
            temp.next=head;
            temp=temp.next;
            list1 = list1.next;
        }
        while(list2!=null)
        {
            ListNode head = new ListNode();
            head.val = list2.val;
            temp.next=head;
            temp = temp.next;
            list2 = list2.next;
        }
        return list;
    }
}