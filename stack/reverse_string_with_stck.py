class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None


    def push(self,data,n):
        self.n=n
        for i in range(n):
            if self.head==None:
                self.head=node(data[i])
                #print("a")
            else:
                temp=node(data[i])
                #print("a")
                temp.next=self.head
                self.head=temp    

    def pop(self,n):
        self.n=n
        if self.head==None:
            print("empty")
           
        else:
            print("reversed data is : ",end="")
            while(n>0 and (self.head is not None)):
                
                popped=self.head
                
                self.head=self.head.next
                popped.next=None
                print(popped.data,end="")
                n-=1

if __name__=="__main__":
    stk=stack()
    str1=input("enter the string here ")
    n=len(str1)
    stk.push(str1,n)
    stk.pop(n)
    
                                             