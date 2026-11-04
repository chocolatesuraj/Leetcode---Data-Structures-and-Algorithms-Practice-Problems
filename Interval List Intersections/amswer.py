class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while i<len(firstList) and j<len(secondList):
            a,b= firstList[i][0],firstList[i][1]
            c,d= secondList[j][0],secondList[j][1]
            if b<c:
                i+=1
            elif a>d:
                j+=1
            else:
                new=[max(a,c),min(b,d)]
                ans.append(new)
                if b>d:
                    j+=1
                else:
                    i+=1

        return ans
