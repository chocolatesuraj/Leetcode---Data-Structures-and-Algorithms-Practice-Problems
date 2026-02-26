class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        f,b=0,0
        temp=set()
        while(b<=k and b<len(nums)):
            # print(temp)
            if nums[b] in temp:
                return True
            else:
                temp.add(nums[b])
                b+=1
        while(b<len(nums)):
            temp.remove(nums[f])
            if nums[b] in temp:
                return True
            temp.add(nums[b])
            b+=1
            f+=1
        return False
