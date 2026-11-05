sys.set_int_max_str_digits(100000)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for n in num:
            if not stack or n>stack[-1]:
                stack.append(n)
            else: 
                while stack and k and stack[-1]>n:
                    stack.pop()
                    k-=1
                stack.append(n)
        while k:
            stack.pop()
            k-=1
        
        ans=""
        flag=True
        for n in stack:
            if flag==True and n=="0":
                continue 
            else:
                flag=False
                ans+=n
        if ans=="":
            return "0"
        return ans
                
        # ans=0
        # mult=1
        # while stack:
        #     ans+=int(stack.pop())*mult
        #     mult*=10
        # return str(ans)
