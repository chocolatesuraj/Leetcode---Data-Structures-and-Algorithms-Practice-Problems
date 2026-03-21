class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dskip=0
        rskip=0
        l=len(senate)*2
        q=deque(senate)
        i=0
        while q and i<l:
            i+=1
            # print(q)
            change=False
            s=q.popleft()
            if s=="R":
                if rskip==0:
                    q.append(s)
                    dskip+=1
                else:
                    rskip-=1
            if s=="D":
                if dskip==0:
                    q.append(s)
                    rskip+=1
                else:
                    dskip-=1
            # print(q)
        s=q.popleft()
        if s=="D":
            return "Dire"
        return "Radiant"
        
