class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#create and link node
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
#display node'
def display():
    global head
    temp = head
    while temp:
        print(temp.data,end="-->")
        temp = temp.next
#delete last node
def delete_last():
    global head
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None

#operation
print("Before Delete")
display()
delete_last()
print("After deletion")
print()
display()