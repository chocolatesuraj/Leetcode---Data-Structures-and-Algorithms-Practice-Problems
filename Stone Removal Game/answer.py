class Solution:
    def canAliceWin(self, n: int) -> bool:
        counter=0
        sub=10
        while n-sub>=0:
            n-=sub
            counter+=1
            sub-=1
        if counter%2==1:
            return True
        return False
