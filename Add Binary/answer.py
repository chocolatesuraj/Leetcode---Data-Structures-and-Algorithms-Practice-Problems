class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=""
        if a=="0" and b=="0":
            return"0"
        carry=0
        a=int(a)
        b=int(b)
        while a or b or carry:
            bit1=0
            bit2=0
            if a:
                bit1=a & 1
                a=a//10
            if b:
                bit2= b & 1
                b=b//10
            total = bit1+bit2+carry
            if total==0:
                ans="0"+ans
            elif total==1:
                ans="1"+ans
                carry=0
            elif total==2:
                carry=1
                ans="0"+ans
            else: #total==3
                ans="1"+ans
                carry=1

        return ans 
