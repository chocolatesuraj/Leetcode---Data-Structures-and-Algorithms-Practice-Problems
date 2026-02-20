class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names={}# email to name hashmap
        union_find={}#key = email , value = parent mail 
        def get_parent(mail):
            # print(union_find)
            while(mail!=union_find[mail]):
                mail=get_parent(union_find[mail])
            return mail
        


        adj=defaultdict(list) # adjustancy l
        for account in accounts:
            name=account[0]
            p_mail=account[1]
            names[p_mail]=name
            if p_mail in union_find:
                p_mail=get_parent(p_mail)
            for mail in account[1:]:
                names[mail]=name
                if(mail in union_find):
                    new_parent=get_parent(mail)
                    union_find[p_mail]=new_parent
                    p_mail=new_parent
                union_find[mail]=p_mail
        # print(union_find)    
        mails=defaultdict(list)
        for email,parent in union_find.items():
            mails[get_parent(parent)].append(email)
        ans=[]
        for p,m in mails.items(): # p= parent , m= child mails 
            new=[]
            new.append(names[p])
            mail_list=m
            mail_list.sort()
            new=new+mail_list
            ans.append(new)
        return ans


        


                    




            
            




