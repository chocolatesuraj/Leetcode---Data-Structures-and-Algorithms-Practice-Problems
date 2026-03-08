class Node:
    def __init__(self,value):
        self.val=value
        self.next=None 
class MyHashSet:

    def __init__(self):
        self.l=pow(10,4)
        self.hashset=[Node(None) for i in range(self.l)]

    def add(self, key: int) -> None:
        pos=key%self.l
        prev=self.hashset[pos]
        curr=prev.next
        while curr != None:
            if(curr.val==key):
                return
            prev=curr
            curr=curr.next
        prev.next=Node(key)    

    def remove(self, key: int) -> None:
        pos=key%self.l
        prev=self.hashset[pos]
        curr=prev.next
        while curr:
            if(curr.val==key):
                prev.next=curr.next
                return
            prev=curr
            curr=curr.next

    def contains(self, key: int) -> bool:
        pos=key%self.l
        node=self.hashset[pos]
        while node != None:
            if(node.val==key):
                return True
            node=node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
