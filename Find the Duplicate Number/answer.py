class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # prevslow
        slow=nums[0]
        fast=nums[slow]

        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
        slow1=nums[0]
        slow2=nums[fast]

        while slow1!=slow2:
            slow1=nums[slow1]
            slow2=nums[slow2]

        return slow1
