# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        size = 0
        while(node):
            size +=1
            node = node.next
        
        target = size - n + 1
        node = head
        prev = None
        for i in range(1, target):
            prev = node
            node = node.next
        if prev and node.next:
            prev.next = node.next
        elif prev:
            prev.next = None
        elif node.next:
            head = node.next
        else:
            return None
        return head