class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,x):
        self.dtemp=node(x)
        self.dtemp.next=self.head
        self.head=self.dtemp    
llist=linkedlist()
for i in range(1,4):
    n=int(input("enter the number "))
    llist.insert(n)
temp=llist.head
print()
while(temp!=None):
    print(temp.data)
    temp=temp.next
    

