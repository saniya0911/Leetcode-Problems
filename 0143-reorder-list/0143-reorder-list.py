# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # node = head
        # while node is not None and node.next is not None:
        #     last = node
        #     prev = last
        #     curr = node
        #     curr_next = curr.next
        #     while(last.next is not None):
        #         prev = last
        #         last = last.next
        #     if curr.next == last:
        #         break
        #     curr.next = last
        #     prev.next = last.next
        #     last.next = curr_next
        #     node = node.next.next
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        while(second):
            curr_next = second.next
            second.next = prev
            prev = second
            second = curr_next
        
        second = prev

        first = head
        while(first and second):
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2