class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n5.prev = n4

def delete_mid(pos):
    global head
    temp = head
    for i in range(pos):
        temp = temp.next
    temp.prev.next = temp.next
    temp.next.prev = temp.prev

def display(head):
    temp = head
    while temp:
        print(temp.data,end = "-->")
    print()
print("Before deletion :")
display(head)
delete_mid(3)
print("Afterdeletion :")
display(head)
