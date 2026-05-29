class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: [x[1],x[2]])
        q=[]
        cap=capacity
        currtime=0
        for pasg,start,end in trips:
            currtime=max(currtime,start)
            while q and q[0][0]<=currtime:
                cap+=q[0][2]
                heapq.heappop(q)
                
            cap-=pasg
            heapq.heappush(q,[end,start,pasg])
            if cap<0:
                return False
        return True 


            
            
