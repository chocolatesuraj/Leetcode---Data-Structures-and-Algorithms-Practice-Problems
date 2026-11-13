class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        ans = [0]* ((n-1)*2+1)
        exp={} # postion -> number expected positon for a number that has been added once.  expected value at position 
        exc=set()
        def func(pos):
            if pos == len(ans):
                return True
            if pos in exp:
                save=ans[pos]
                ans[pos]=exp[pos]
                if func(pos+1):
                    return True 
                ans[pos]=save
                return False
                    

            for num in range(n,0,-1):
                if (num not in exc) and ((pos+num not in exp) or num==1):
                    if pos+num>=len(ans) and num!=1:
                        return False
                    ans[pos]=num
                    if num!=1 :
                        exp[pos+num]=num
                    
                    exc.add(num)
                    
                    if func(pos+1):
                        return True
                    else:
                        if num!=1 :
                            del exp[pos+num]
                        exc.remove(num)
                        ans[pos]=0
                        continue 
                # else:
                    # print(num,(num not in exp),(num not in exc),(pos+num not in exp))

        func(0)
        return ans



