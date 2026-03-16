class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        a=0 # even spots lesser, odd spots more  
        b=0 # odd spots lesser ,even spots more
        ans=0
        for i,num in enumerate(arr):
            if i%2==0:
                if i==0:
                    a+=1
                    b+=1
                elif arr[i-1]<num:
                    a+=1
                    b=1
                elif  arr[i-1]>num:
                    a=1
                    b+=1
                else:
                    a=1
                    b=1
            elif i%2==1:
                if arr[i-1]<num:
                    b+=1
                    a=1
                elif  arr[i-1]>num:
                    b=1
                    a+=1
                else:
                    a=1
                    b=1
            ans=max(ans,a,b)
        return ans

            
