class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo=[None]*len(nums)
        def dp(pos,nums):
            #rob pos 
            if pos>=len(nums):
                return 0
            if memo[pos]!=None:
                return memo[pos]
            r1=nums[pos]+dp(pos+2,nums)
            #skip pos
            r2=dp(pos+1,nums)
            maxrob=max(r1,r2)
            memo[pos]=maxrob
            return maxrob

        a=dp(0,nums[0:-1])
        memo=[None]*len(nums)
        b=dp(0,nums[1:])
        return max(a,b)

        

        
