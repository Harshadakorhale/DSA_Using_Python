#define node class
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
#Initialize head as null
head = None
#fun to insert node at first 
def insert_at_beginning(data):
    global head
    newnode = Node(data)
    if head is None:
        head = newnode
    else:
        newnode.next = head
        head.prev = newnode
        head = newnode
#fun to dispaly the DLL
def dispaly():
    global head
    temp = head
    while temp:
        print(temp.data,end = "-->")
        temp = temp.next
    print("NULL")
insert_at_beginning(10)
insert_at_beginning(20)
insert_at_beginning(30)
dispaly()
