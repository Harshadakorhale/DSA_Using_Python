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

def insert_at_pos(pos, data):
    global head
    new = Node(data)
    temp = head
    count = 1
    while count<pos-1:
        temp = temp.next
        count+=1
    new.next = temp.next
    temp.next = new

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
insert_at_pos(2,50)
print("After Insertion:")
display()


