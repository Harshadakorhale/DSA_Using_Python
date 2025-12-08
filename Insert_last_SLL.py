#create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#create the head node
head = Node(10)
#add node at end
def add_last(head,data):
    newnode = Node(data)
    temp = head
    while temp.next:
        temp = temp.next
        temp.next = newnode
#add node
add_last(20)
add_last(30)
#print list
def print_list(head):
    temp = head
    while temp:
        print(temp.data,end="-->")
        temp = temp.next
print("NULL")
#display list
print_list(head)

