class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def func(cursum,node):
            if node==None:
                return 0
            newsum=cursum*10+node.val
            if node.right==None and node.left==None:
                self.ans+=newsum
                return
            func(newsum,node.right)
            func(newsum,node.left)
        func(0,root)
        return self.ans
