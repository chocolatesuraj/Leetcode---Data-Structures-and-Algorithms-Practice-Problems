class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<=0:
            return max(nums)

        fsums=[0]*len(nums)
        bsums=[0]*len(nums)

        fsum=0
        maxfsum=-float("inf")
        for i,num in enumerate(nums):
            fsum+=num
            maxfsum=max(maxfsum,fsum)
            fsums[i]=maxfsum
            
        bsum=0
        maxbsum=-float("inf")
        for i in range(len(nums)-1,-1,-1):
            bsums[i]=maxbsum
            num=nums[i]
            bsum+=num
            maxbsum=max(maxbsum,bsum)
        # print(bsums)    
        
        tempsum=0
        maxsum=-float("inf")
        for i,num in enumerate(nums):
            if tempsum+num>=0:
                tempsum+=num
                maxsum=max(maxsum,tempsum)
            else:tempsum=0
        ans=-float("inf")
        for i in range(len(nums)):
            ans=max(ans,fsums[i]+bsums[i])
        
        return max(maxsum,ans)
        



        

            
            
