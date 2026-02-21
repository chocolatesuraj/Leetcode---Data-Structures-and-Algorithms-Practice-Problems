class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}
        ans=0
        def dfs(targ):
            if(targ in memo):
                return memo[targ]
            p=0
            for num in nums:
                if(targ-num==0):
                    p+=1
                if(targ-num>0):
                    p+=dfs(targ-num)
            memo[targ]=p
            return p

        return dfs(target)
        

