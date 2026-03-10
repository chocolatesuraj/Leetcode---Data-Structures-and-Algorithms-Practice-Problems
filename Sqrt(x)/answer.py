class Solution:
    def mySqrt(self, x: int) -> int:
        f,b=0,x
        m=0
        res=0
        while(f<=b):
            m=int( (f+b)//2 ) 
            sq=m*m
            prevf=f
            prevb=b
            
            if(sq>x):
                b=m-1
            elif(sq<x):
                f=m+1
                res=max(res,m)
            elif(sq==x):
                return m

        return res
