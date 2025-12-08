#define node class
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
#Initialize head as null
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
head.next = n2
n2.next = n3
n2.prev = head
n3.next = n4
n3.prev = n2
n4.next = n5
n4.prev = n3
n5 .prev = n4

def insert_at_pos(head,pos,data):
    newnode = Node(data)
    temp = head
    count = 1
    while count < pos-1:
        temp = temp.next
        count = count+1
    newnode.next = temp.next
    newnode.prev = temp
    temp.next.prev = newnode
    temp.next = newnode
    
def display(head):
    temp = head
    while temp:
        print(temp.data,end = "-->")
        temp = temp.next
    print("Null")
insert_at_pos(head,3,25)
display(head)

