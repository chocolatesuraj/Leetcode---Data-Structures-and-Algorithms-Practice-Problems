class LFUCache:

    def __init__(self, capacity: int):
        self.kv = defaultdict(int)
        self.kf = defaultdict(int)
        self.fk = defaultdict(OrderedDict) 
        self.min = None
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.kv:
            ans = self.kv[key]
            currfreq = self.kf[key]
            self.kf[key]=currfreq+1
            self.fk[currfreq+1][key]=None
            del self.fk[currfreq][key]

            if len(self.fk[currfreq])==0 and self.min == currfreq:
                self.min=currfreq+1
            return ans
        else:
            return  -1       

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.kv[key]=value
            self.get(key)
            return 
            
        if (len(self.kv)==self.capacity):
            minfreq = self.min
            delkey,_ = self.fk[minfreq].popitem(last=False)
            del self.kv[delkey]
            # del self.fk[minfreq][delkey]
            del self.kf[delkey]

        self.kv[key]=value
        self.kf[key]=1
        self.fk[1][key]=None
        self.min=1
            
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
