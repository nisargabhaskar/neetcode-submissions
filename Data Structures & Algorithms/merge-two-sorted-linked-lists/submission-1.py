# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2 = list1,list2
        if not curr1 or not curr2:
            return curr1 if curr1 else curr2
        if curr1.val < curr2.val:
            temp = curr1.next
            curr1.next = None
            res = curr1
            curr1 = temp
        else :
            temp = curr2.next
            curr2.next = None
            res = curr2
            curr2 = temp
        resptr = res
        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp = curr1.next
                curr1.next = None
                resptr.next = curr1
                curr1 = temp
            else:
                temp = curr2.next
                curr2.next = None
                resptr.next = curr2
                curr2 = temp
            resptr = resptr.next
        if curr1:
            resptr.next = curr1
        if curr2:
            resptr.next = curr2
        return res