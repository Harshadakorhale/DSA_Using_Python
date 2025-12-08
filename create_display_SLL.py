#create a node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
#link node 
node1.next = node2
node2.next = node3
#Assign head
head = node1
#Display LL
temp = head
while temp:
    print(temp.data, end="-->")
    temp = temp.next
print("NULL")
