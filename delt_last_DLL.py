class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None      # Extra pointer for DLL

# Create and link nodes
head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# Linking forward
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Linking backward
n2.prev = head
n3.prev = n2
n4.prev = n3
n5.prev = n4

# Display DLL
def display():
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

# Delete last node in DLL
def delete_last():
    global head
    if head is None:
        print("List is empty")
        return
    
    temp = head

    # If only one node
    if temp.next is None:
        head = None
        return

    # Traverse to last node
    while temp.next is not None:
        temp = temp.next

    # Remove last node
    temp.prev.next = None


# Operation
print("Before Deletion:")
display()

delete_last()

print("After Deletion:")
display()
