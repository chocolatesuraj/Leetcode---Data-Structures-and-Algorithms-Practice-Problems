class Solution:
    def numSquares(self, n: int) -> int:
        sqrs=deque()
        i=1
        while(i*i<=n):
            sqrs.appendleft(i*i)
            i+=1
        memo={}
        def dfs(num):
            if(num in memo):
                return memo[num]
            ret=float("inf")
            for s in sqrs:
                if(num-s==0):
                    memo[num]=1
                    return 1
                if(num-s>0):
                    ret=min(ret,1+dfs(num-s)) 
            memo[num]=ret
            return ret 
                
        return dfs(n)
