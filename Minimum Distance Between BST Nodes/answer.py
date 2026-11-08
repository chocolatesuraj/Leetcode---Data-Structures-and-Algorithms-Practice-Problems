# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=float('inf')
        
        def func(node):
            if node==None:
                return float('inf'),-float('inf')
            if node.right == None and node.left == None:
                return node.val,node.val
            nonlocal ans
            mini1,maxi1=func(node.right)
            mini2,maxi2=func(node.left)
            ans=min(ans,node.val-maxi2)
            ans=min(ans,mini1-node.val)
            return (min(mini2,node.val),max(node.val,maxi1 ))

        func(root)
        return ans

                
