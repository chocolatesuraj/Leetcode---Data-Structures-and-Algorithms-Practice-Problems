class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if nums==[1]:
            return True
        nums=list(set(nums))
        if len(nums)==1 and nums[0]!=1:
            return True
        if len(nums)==1 and nums[0]==1:
            return False
        
        
        adj=defaultdict(list)

        union=defaultdict(list) # list =[parent,rank]
        for num in nums:
            union[num] = [num,0]

        def parent(node):
            if union[node][0] != node :
                union[node][0] = parent(union[node][0])
            return union[node][0]

        def merge(src,dst):
            if src not in union:
                union[src]=[src,0]
            if dst not in union:
                union[dst]=[dst,0]
            ps=parent(src)
            pd=parent(dst)

            if union[ps][1]>union[pd][1]:
                union[pd][0]=ps
            elif union[ps][1] == union[pd][1]:
                union[pd][0]=ps
                union[ps][1]+=1
            else:
                union[ps][0]=pd
       
        for num in nums:
            x=num
            d=2
            while(d*d<=x):
                if x%d==0:
                    merge(num,d)
                    while(x%d==0):
                        x=x//d
                d+=1
            if x>1:
                merge(num,x)
        
        
        gparent=parent(nums[0])
        for num in nums:
            if parent(num)!=gparent:
                return False
        return True

                
       

