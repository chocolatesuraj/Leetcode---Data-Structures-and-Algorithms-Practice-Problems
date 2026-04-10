# def Node:
#     def __init__(self,val,freq=1):
#         self.val=val
#         self.freq=freq
class FreqStack:

    def __init__(self):
        self.hashmap = defaultdict(int) # val -> freq
        self.freqmap = {} # freq -> [stack of vals] 
        self.maxstack=[]
    def push(self, val: int) -> None:
        if self.hashmap[val] not in self.freqmap:
            self.freqmap[self.hashmap[val]]=[]

        self.hashmap[val]+=1
        if self.hashmap[val] not in self.freqmap:
            self.freqmap[self.hashmap[val]]=[]
        self. freqmap[self.hashmap[val]].append(val)

        if self.maxstack==[] or self.hashmap[val]>self.maxstack[-1]:
            self.maxstack.append(self.hashmap[val])
 

    def pop(self) -> int:
        top=self.maxstack[-1]
        ans=self.freqmap[top].pop()
        if len(self.freqmap[top])==0:
                self.maxstack.pop()
        self.hashmap[ans]-=1
        return ans 
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
