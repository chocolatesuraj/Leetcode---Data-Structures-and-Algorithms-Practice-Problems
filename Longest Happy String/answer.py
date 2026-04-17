class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        if a != 0:
            heapq.heappush(heap,[-a,"a"])
        if b!=0:
            heapq.heappush(heap,[-b,"b"])
        if c!=0:
            heapq.heappush(heap,[-c,"c"])
        ans=""
        while heap:
            count,top=heapq.heappop(heap)
            count=-count
            if len(ans)<2 or ans[-1]!=ans[-2] or top!=ans[-1]:
                ans+=top
                if count-1>0:
                    heapq.heappush(heap,[-(count-1),top])
            else:
                if len(heap)==0:
                    return ans 
                else: 
                    count2,top2=heapq.heappop(heap)
                    count2=-count2
                    ans+=top2
                    if count2-1>0:
                        heapq.heappush(heap,[-(count2-1),top2])
                    heapq.heappush(heap,[-count,top])
        return ans 
