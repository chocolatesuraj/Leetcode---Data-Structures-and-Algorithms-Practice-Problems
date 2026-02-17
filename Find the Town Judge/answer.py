class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        trusters=defaultdict(set) #person: all peeople that trust that person
        trustee=defaultdict(set)  #person: all people that person trusts
        
        for src,dest in trust:
            trusters[dest].add(src)
            trustee[src].add(dest)

        ans=None
        count=0
        for person,t in trusters.items():
            if(len(t)==n-1 and len(trustee[person])==0 ):
                return person
        
        return -1
        


                
