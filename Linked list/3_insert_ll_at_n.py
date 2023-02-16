class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def ninsert(self,x,n):
        self.temp1=node(x)
        if(n==1): #if position to insert is 1
            self.temp1.next=self.head
            self.head=self.temp1
            return
        self.temp2=self.head #if n is not 1 create an iterator variable and assign it value of head
        for i in range(1,n-1):  #find n-2th positional node for loop will end at n-2
            self.temp2=self.temp2.next 
        self.temp1.next=self.temp2.next #change links and insert temp1
        self.temp2.next=self.temp1
        return    
        #to reverse linked list
    def reverse(self):
        self.current=self.head #create current and prev and set prev to None
        self.prev=None
        while(self.current!=None): #lood untill end of llist
            self.next=self.current.next  #this self.next is a class variable here
            self.current.next=self.prev
            self.prev=self.current
            self.current=self.next   
        self.head=self.prev
    def print(self):   
        self.temp=self.head
        while(self.temp!=None):
            print(self.temp.data,end="->")
            self.temp=self.temp.next 
        print()
llist=linkedlist()

llist.ninsert(1,1)

llist.ninsert(14,2)
llist.ninsert(44,2)
llist.ninsert(18,3)
llist.ninsert(198,1)
llist.print()
    
#reverse linked list
llist.reverse()
llist.print()