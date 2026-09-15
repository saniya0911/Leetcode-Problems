# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        s = l1.val + l2.val
        head = ListNode(s%10)
        carry = s//10
        node = head
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            s = l1.val + l2.val + carry
            node.next = ListNode(s%10)
            node = node.next
            carry = s//10
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + carry
            node.next = ListNode(s%10)
            node = node.next
            carry = s//10
            l1 = l1.next

        while l2:
            s = l2.val + carry
            node.next = ListNode(s%10)
            node = node.next
            carry = s//10
            l2 = l2.next
            
        if carry != 0:
            s = carry
            node.next = ListNode(s%10)
            node = node.next
            carry = s//10

        return head