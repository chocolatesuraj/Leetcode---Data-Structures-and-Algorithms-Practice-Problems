class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        store=deque()
        ans=[]
        for i,num in enumerate(nums):
            if store and store[0][1]<=i-k:
                store.popleft()
            
            while(len(store)>0 and num>=store[-1][0]):
                    store.pop()
            store.append([num,i])
            
            if i>=k-1:
                ans.append(store[0][0])
        return ans
