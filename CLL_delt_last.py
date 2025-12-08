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

def delete_last():
    global head
    temp = head
    while temp.next.next != head:
        temp = temp.next
    temp.next = head

def display():
    global head
    temp = head
    while True:
        print(temp.data,end ="-->")
        temp = temp.next
        if temp==head:
            break

print("Before Deletion:")
display()
print()
delete_last()
print("After Deletion:")
display()  