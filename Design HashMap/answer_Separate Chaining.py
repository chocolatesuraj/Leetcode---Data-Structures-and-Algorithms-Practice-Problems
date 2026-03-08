class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.nextele=None 
class MyHashMap:

    def __init__(self):
        self.l=pow(10,4)
        self.hashset=[Node(None,None) for i in range(self.l)]

    def put(self, key: int, value: int) -> None:
        pos=key%self.l
        
        prev=self.hashset[pos]
        curr=prev.nextele
        while curr != None:
            if(curr.key==key):
                curr.val=value
                return
            prev=curr
            curr=curr.nextele
        prev.nextele=Node(key,value)  

    def get(self, key: int) -> int:
        pos=key%self.l
        node=self.hashset[pos]
        while node != None:
            if(node.key==key):
                return node.val
            node=node.nextele
        return -1
        

    def remove(self, key: int) -> None:
        pos=key%self.l
        prev=self.hashset[pos]
        curr=prev.nextele
        while curr:
            if(curr.key==key):
                prev.nextele=curr.nextele
                return
            prev=curr
            curr=curr.nextele
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
