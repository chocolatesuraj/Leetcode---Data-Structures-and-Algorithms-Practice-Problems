class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        leng=len(nums)
        visited=set()
        for i in range(0,leng):
            if nums[i] in visited:
                return nums[i]
            visited.add(nums[i])
            
