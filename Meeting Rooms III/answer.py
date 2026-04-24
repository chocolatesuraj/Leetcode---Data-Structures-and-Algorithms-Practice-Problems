class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meets=[]
        minroom=[]
        
        for i in range(0,n):
            heapq.heappush(minroom,i)

        heapq.heapify(meetings)
        meets=meetings

        counts=[0]*n
        rooms=[]
        while meets:
            start,end=heapq.heappop(meets)
            while len(rooms)>0 and rooms[0][0]<=start:
                    olde,oldroom,olds=heapq.heappop(rooms)
                    heapq.heappush(minroom,oldroom)

            diff=0
            if len(rooms)==n:
                olde,oldroom,olds=heapq.heappop(rooms)
                heapq.heappush(minroom,oldroom)
                if olde>start:
                    diff=olde-start
            mr=heapq.heappop(minroom)
            heapq.heappush(rooms,[end+diff,mr,start])
            counts[mr]+=1
            
                
                
        maxi=0
        maxmeets=0
        mini=float("inf")
        flag=True
        for roomnum,meets in enumerate(counts):
            if meets>maxi:
                maxi=meets
                maxpos=roomnum
        return maxpos



            
