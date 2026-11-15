class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr=[]
        pos=0 
        remletter={}
        remletter[0]=[1,2]
        remletter[1]=[0,2]
        remletter[2]=[0,1]

        base=None
        if k>3*pow(2,n-1):
            return ""
        while(pos<n):
            # print(pos,base,curr)
            if pos==0:
                for i in range(3):
                    groupmax=(i+1)*pow(2,n-pos-1)
                    # print(groupmax)
                    if k<=groupmax:
                        curr.append(i)
                        base=(i)*pow(2,n-pos-1)
                        break
                        
            elif pos!=0:
                groups=remletter[curr[-1]]
                # print("grpssssssss",groups)
                for i,group in enumerate(groups):
                    groupmax=base+(i+1)*pow(2,n-pos-1)
                    # print(groupmax)
                    if k<=groupmax:
                        curr.append(group)
                        base+=(i)*pow(2,n-pos-1)
                        break
            pos+=1
        ans=""
        for l in curr:
            if l==0:
                ans+="a"
            if l==1:
                ans+="b"
            if l==2:
                ans+="c"
        return ans


