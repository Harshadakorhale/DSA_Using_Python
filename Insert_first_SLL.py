#create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#start with empty list
head = None
#insert at 1st Position
def insert_f(head,data):
    newnode = Node(data)
    newnode.next = head
    head = newnode
    return head
#insert node
head = insert_f(head,30)
head = insert_f(head,20)
head = insert_f(head,10)
#dispaly list
temp =head
while temp:
    print(temp.data,end ="-->")
    temp = temp.next
print("NULL")