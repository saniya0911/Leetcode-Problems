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
        node = head
        while node is not None and node.next is not None:
            last = node
            prev = last
            curr = node
            curr_next = curr.next
            while(last.next is not None):
                prev = last
                last = last.next
            if curr.next == last:
                break
            curr.next = last
            prev.next = last.next
            last.next = curr_next
            node = node.next.next

        