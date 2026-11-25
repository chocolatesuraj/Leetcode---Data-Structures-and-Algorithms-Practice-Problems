# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        def getval(node):
            ans=0
            while node:
                ans=ans*10+node.val
                node=node.next
            return ans 

        a=getval(l1)
        b=getval(l2)
        c=a+b
        ans=None
        if c==0:
            return ListNode(0,ans)
        while(c):
            if c//10==0 and c%10==0:
                return ans
            num=c%10
            node=ListNode(num,ans)
            ans=node
            c=c//10
        return ans
