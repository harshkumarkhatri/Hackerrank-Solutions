class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        #firstly we will check if the condition is true or not.
        #if we have none as head then the element will store at first position           with null as a next pointing node
        if head==None:
            head=Node(data)
        #if above condition false then we take the head as curr i.e. a variable          which takes the address of the first node and checks the condition if           any further nodes are present. If no more nodes present then the first          node address will be replaced with the current node address and the             current node address will have pointing address as null.
        else:
            curr=head
            while curr.next:
                curr=curr.next
            curr.next=Node(data)
            #storing the data at the node with respective pointing address.
        return head
        #return the head i.e. the data stored

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  