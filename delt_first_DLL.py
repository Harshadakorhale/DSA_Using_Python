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

def delete_first():
    global head
    if head is None:
        print("List is empty")
    else:
        temp = head
        head = head.next
        head.prev = None

def display(head):
    temp = head
    while temp:
        print(temp.data,end="-->")
        temp = temp.next
    print()
print("Before deletion")
display(head)
delete_first
print("After deletion")
display(head)
