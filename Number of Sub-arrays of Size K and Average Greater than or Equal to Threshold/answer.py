class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        f,b=0,0
        s=0
        s=arr[0]
        ans=0
        while (b<len(arr)):
            if b-f<k-1:
                b+=1
                s+=arr[b]
            elif b-f == k-1:
                avg=s/k
                if avg>=threshold:
                    ans+=1
                s-=arr[f]
                f+=1
                b+=1
                if b<len(arr):
                    s+=arr[b]
        return ans

                
