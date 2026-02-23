class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        stack=deque()
        stack.append(0)
        maxpos=0
        while(stack):
            pos=stack.popleft()
            if(pos==len(s)-1):
                return True
            for i in range(max(pos+minJump,maxpos+1),min(pos + maxJump, len(s) - 1)+1):
                maxpos=i

                if(s[i]=="0"):
                    stack.append(i)
                    if i == len(s)-1:
                        return True
        return False
        
