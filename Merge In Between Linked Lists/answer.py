# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p1=list1
        p2=list2
        for i in range(a-1):
            p1=p1.next

        newp1=p1.next
        p1.next=list2
        while p1.next:
            p1=p1.next

        for i in range(b-a+1):
            newp1=newp1.next
        
        p1.next=newp1

        return list1
            
