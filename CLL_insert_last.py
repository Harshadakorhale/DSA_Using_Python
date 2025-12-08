class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = head


def insert_last(data):
    global head
    new = Node(data)
    if head is None:
        head = new
        new.next = head
    else:
        temp = head
        while temp.next != head :
          temp = temp.next
    temp.next = new
    new.next = head

def display():
    global head
    temp = head
    while True:
        print(temp.data,end ="-->")
        temp = temp.next
        if temp==head:
            break

print("Before Insertion:")
display()
print()
insert_last(50)
print("After Insertion:")
display()

