class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        n/3 n/3 n/3
        n/3+1 n/3-2 n/3+1
        """
        minlen=len(nums)/3
        num1,num2,count1,count2=None,None,None,None
        
        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
            elif num1==None:
                num1=num
                count1=1
            elif num2==None:
                num2=num
                count2=1
            

            else:
                count1-=1
                count2-=1
                if count1==0:
                    count1=None
                    num1=None
                if count2==0:
                    count2=None
                    num2=None
            # print(num," ",num1,count1,num2,count2)
            
        # print(num1,num2)
        count1=0
        count2=0
        ans=[]
        for num in nums:
            if num==num1:
                count1+=1
            elif num==num2:
                count2+=1
        if count1>minlen:
            ans.append(num1)
        if count2>minlen:
            ans.append(num2)
        return ans 

            

        
        
    


            
                


                

        

            
                
