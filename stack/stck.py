class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head==None:
            return True
        else:
            return False    
            
    #method to push into stack
    def push(self,data):
        #temp=node(data)
        if self.head==None:
            self.head=node(data)
        else: 
            temp=node(data)   
            temp.next=self.head
            self.head=temp


    def pop(self):
        if self.isempty():
            return None
        else:    
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
        return popped_node.data
    def top(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
  
        else:
            print()
            while(iternode!= None):
  
                print(iternode.data, end = "")
                iternode = iternode.next
                if(iternode != None):
                    print(" -> ", end = "")
            return  

if __name__=="__main__":
                                
    stk=stack()
    stk.display()
    stk.push(7)
    stk.display()
    stk.push(5)
    stk.push(3)                        
    stk.display()
    stk.pop()

    stk.display()
