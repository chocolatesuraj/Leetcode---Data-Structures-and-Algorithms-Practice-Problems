class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo=[[None]*len(nums) for i in range(len(nums))]
        def dp(r,f,b,l):
            # key=str(f)+" "+str(b)+" " #+str(l) 
            if(f>b):
                return 0
            if(memo[f][b] != None):
                return memo[f][b]
            if f==b:
                maxcoins = r*nums[f]*l
                memo[f][b]=maxcoins
                return maxcoins
            maxcoins=0
            for i  in range(f,b+1):
                coins=nums[i]*r*l+dp(r,f,i-1,nums[i])+dp(nums[i],i+1,b,l)
                maxcoins=max(coins,maxcoins)
            memo[f][b]=maxcoins
            return maxcoins
        return dp(1,0,len(nums)-1,1)


