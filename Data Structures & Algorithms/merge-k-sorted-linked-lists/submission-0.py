# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        while any([True for i in lists if i is not None]):
            minval = lists[0].val 
            minidx = 0
            for i in range(len(lists)):
                if lists[i].val < minval:
                    minidx = i
                    minval = lists[i].val
            dummy.next = ListNode(minval)
            if lists[minidx].next:
                lists[minidx] = lists[minidx].next
            else:
                lists.pop(minidx)
            dummy = dummy.next
        return res.next


