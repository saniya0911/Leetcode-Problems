# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        merged = []
        for l in lists:
            while l:
                merged.append(l)
                l = l.next
        if not merged:
            return None
        merged.sort(key = lambda node:node.val)
        for i in range(1, len(merged)):
            merged[i-1].next = merged[i]

        return merged[0]
