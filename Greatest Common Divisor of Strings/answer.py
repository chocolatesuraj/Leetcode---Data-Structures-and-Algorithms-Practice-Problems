class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans=""
        l1=len(str1)
        l2=len(str2)
        i=0
        while(i<l1 and i<l2):
            if str1[i] ==str2[i]:
                divisor=str1[0:i+1]
                dl=len(divisor) 
                if divisor*(int(l1/dl))==str1 and divisor*(int(l2/dl))==str2 and int(l1/dl) == l1/dl  and int(l2/dl) == l2/dl:
                    ans=divisor
            i+=1
            
        return ans
