#create node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#initialize head to null
head = None
#add node
def add_last(data):
    global head
    newnode = Node(data)
    if head is None:
        head = newnode
        return
    temp = head
    while temp.next:
        temp = temp.next
        temp.next = newnode
#function todelete 1st node
def delete_f():
    global head
    if head is None:
        print("List is empty")
    else:
        temp = head
        head = head.next
        del temp
#display function
def display():
    temp = head
    while temp:
        print(temp.data,end = "-->")
        temp = temp.next
print("NULL")
add_last(10)
add_last(20)
add_last(30)
add_last(40)
print("Before deletion")
display()
delete_f()
print("After deletion")
display()
