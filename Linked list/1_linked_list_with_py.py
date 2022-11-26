"""to create a linked list in python we need to create a class that will help to initiallise a node
and a class that will initiallise a linked list"""

#node class
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
#class fo creating a linked list

class linkedlist:
    def __init__(self):
        self.head=None
        

