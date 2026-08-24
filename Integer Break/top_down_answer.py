class Solution:
    def integerBreak(self, n: int) -> int:
        self.ans=0
        memo={}
    
        def maxprod(num):
            if num in memo:
                return memo[num]
            if(num!=n):
                ret=num
            else:
                ret=0
            for i in range(1,int(num/2)+1):
                a= max(maxprod(i) * maxprod(num-i),i*(num-i))
                ret=max(a,ret)
            self.ans=max(self.ans,ret)
            # print(num,ret)
            memo[num]=ret
            return ret 
        maxprod(n)
        return self.ans
                 
