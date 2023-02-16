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
    #recursive functioin 
    
    '''def reverse(self,item):
        if item.next == None:
            self.head = item
            return
        self.reverse(item.next)
        temp = item.next
        temp.next = item
        item.next = None'''

#recursivley reverse the list
    def revrec(self,p):
        
        if p.next is None:
            self.head=p
            return
        self.revrec(p.next)
        q=p.next
        q.next=p
        p.next=None    

        
        
      

    def print(self):   
        self.temp=self.head
        while(self.temp!=None):
            print(self.temp.data,end="->")
            self.temp=self.temp.next 
        print()

llist=linkedlist()

llist.ninsert(1,1)

llist.ninsert(14,2)
llist.ninsert(44,3)
llist.ninsert(18,4)
llist.ninsert(198,5)
llist.revrec(llist.head)
#llist.reverse(llist.head)
llist.print()
