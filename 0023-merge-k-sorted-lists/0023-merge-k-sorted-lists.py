# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def divideconquer(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left+right)//2
        l1 = self.divideconquer(lists, left, mid)
        l2 = self.divideconquer(lists, mid+1, right)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        if(l1.val<l2.val):
            l1.next = self.merge(l1.next, l2)
            return l1

        else:
            l2.next = self.merge(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # merged = []
        # for l in lists:
        #     while l:
        #         merged.append(l)
        #         l = l.next
        # if not merged:
        #     return None
        # merged.sort(key = lambda node:node.val)
        # for i in range(1, len(merged)):
        #     merged[i-1].next = merged[i]

        # return merged[0]
        return self.divideconquer(lists, 0, len(lists) - 1)

