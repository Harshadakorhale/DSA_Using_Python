#create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# create a list
head = Node(10)
second = Node(20)
third = Node(30)
head.next = second
second.next = third
#insert 30 at 3rd position
newnode = Node(30)
newnode.next = second.next
second.next = newnode
#display list
temp = head
while temp: 
    print(temp.data,end="-->")
    temp = temp.next
print("NULL")