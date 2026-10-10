class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w=0
        r=0
        while(r<len(nums)):
            if nums[r]==0:
                r+=1
            elif nums[r]!=0:
                nums[w]=nums[r]
                r+=1
                w+=1
        while(w<len(nums)):
            nums[w]=0
            w+=1
                

        
