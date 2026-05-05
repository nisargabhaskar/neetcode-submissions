# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp,fp = head,head.next
        while sp and fp:
            if sp == fp:
                return True
            else :
                sp = sp.next
                fp = fp.next.next if fp.next else None
        return False