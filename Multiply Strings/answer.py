class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans=0
        carry=0
        for i,n2 in enumerate(num2[::-1]):
            n2=ord(n2)-ord("0")
            for j,n1 in enumerate(num1[::-1]):
                n1=ord(n1)-ord("0")
                m=n2*n1+carry
                carry=m//10
                mul=m-(carry*10)
                ans+=mul*pow(10,i)*pow(10,j)
            ans+=carry*pow(10,i)*pow(10,j+1)
            carry=0
        return str(ans)



        
