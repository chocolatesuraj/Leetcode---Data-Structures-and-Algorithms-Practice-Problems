# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def dfs(node):
            if(node==None):
                return [0,0]
            if(node.right==node.left==None):
                return [node.val,0] #rob,no rob
            rob_right=dfs(node.right)
            rob_left=dfs(node.left)
            return [node.val+rob_right[1]+rob_left[1],max(rob_right[0],rob_right[1])+max(rob_left[0],rob_left[1])]

        return max(dfs(root))


        
