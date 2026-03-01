class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch.isnumeric():
                prev=0
                if stack and isinstance((stack[-1]),int):
                    prev=stack.pop()
                stack.append(prev*10 +int(ch))

            elif ch=="]":
                string=""
                while(stack[-1]!="["):
                    ele=stack.pop()
                    string=ele+string
                
                a=stack.pop() # remove openig bracaket
                mul=stack.pop() 
                stack.append(string*mul)
            else:
                stack.append(ch)
        ans=""
        for s in stack:
            ans+=s
        return ans


