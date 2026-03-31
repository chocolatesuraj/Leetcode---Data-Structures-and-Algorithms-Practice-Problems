class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def rotate(f,b):
            while(f<b):
                nums[f],nums[b]=nums[b],nums[f]
                f+=1
                b-=1
        rotate(0,len(nums)-1)
        rotate(0,k-1)
        rotate(k,len(nums)-1)
        
