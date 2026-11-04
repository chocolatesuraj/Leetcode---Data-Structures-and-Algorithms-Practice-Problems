class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key= lambda x :x[1])
        prev=None
        l=0
        for pair in pairs:
            if prev==None or pair[0]>prev:
                prev=pair[1]
                l+=1
        return l
        pass

        
