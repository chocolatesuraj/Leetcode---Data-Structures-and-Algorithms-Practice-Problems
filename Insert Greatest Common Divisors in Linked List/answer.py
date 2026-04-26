# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while a!=0:
                a,b=b%a,a
            return b
        node=head
        while node and node.next!=None:
            g=gcd(node.val,node.next.val)
            new=ListNode(g)
            new.next=node.next
            node.next=new
            node=node.next.next
        return head
