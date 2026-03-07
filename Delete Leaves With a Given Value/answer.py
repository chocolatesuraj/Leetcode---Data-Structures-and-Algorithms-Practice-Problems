# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if(node==None):
                return None
            # print(node.val,node.right,node.left)
            
            if(node.right==None and node.left==None and node.val==target):
                return None
            else:
                node.right=dfs(node.right)
                node.left=dfs(node.left)
                if(node.right==None and node.left==None and node.val==target):
                    return None
                return node
        return dfs(root)
