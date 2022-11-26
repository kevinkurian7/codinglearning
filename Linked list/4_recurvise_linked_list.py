class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None

    def ninsert(self,x,n):
        self.temp1=node(x)
        if(n==1):
            self.temp1.next=self.head
            self.head=self.temp1
            return
        self.temp2=self.head
        for i in range(1,n-1):
            self.temp2=self.temp2.next
        self.temp1.next=self.temp2.next
        self.temp2.next=self.temp1
        return  

    def printf(self):
        self.recp(self.head) 

    def recp(self,head1):
        
        if head1 is None:
            return
        print(head1.data,end="->")
        self.recp(head1.next)      

    def reverse_printf(self):
        self.rev_recp(self.head)       

    def rev_recp(self,head1):
        if head1 is None:
            return
        self.rev_recp(head1.next) 
        print(head1.data,end="->")        
        

llist=linkedlist()

llist.ninsert(1,1)

llist.ninsert(14,2)
llist.ninsert(44,2)
llist.ninsert(18,3)
llist.ninsert(198,1)
print("recursively printed")
llist.printf()
print("\n")
print("printed in reverse order with recursion")
llist.reverse_printf()
    