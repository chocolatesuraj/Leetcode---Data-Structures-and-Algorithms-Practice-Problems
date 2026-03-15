class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        tempsum=0
        tempminsum=0
        minsum=float("inf")
        maxsum=-float("inf")
        total=0
        for i,num in enumerate(nums):
            total+=num
            if tempsum+num>=0:
                tempsum+=num
                maxsum=max(maxsum,tempsum)
            else:tempsum=0

            if tempminsum+num<0:
                tempminsum+=num
                minsum=min(minsum,tempminsum)
            else:
                tempminsum=0
        return max(maxsum,total-minsum)
        
        



        

            
            
