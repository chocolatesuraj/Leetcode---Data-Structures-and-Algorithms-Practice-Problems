# def Node:
#     def __init__(self,val,freq=1):
#         self.val=val
#         self.freq=freq
class FreqStack:

    def __init__(self):
        self.hashmap=defaultdict(int)
        self.heap=[]
        self.counter=0

    def push(self, val: int) -> None:
        self.hashmap[val]+=1
        heapq.heappush(self.heap,[-self.hashmap[val],-self.counter,val])
        self.counter+=1
        
    def pop(self) -> int:
        _,_,num=heapq.heappop(self.heap)
        self.hashmap[num]-=1
        if self.hashmap[num]==0:
            del self.hashmap[num]
        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
