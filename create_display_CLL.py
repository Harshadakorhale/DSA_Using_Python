# Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -----------------------------
# CREATE CIRCULAR LINKED LIST
# -----------------------------
def create_circular_list(values):
    head = None
    temp = None

    for val in values:
        newnode = Node(val)

        if head is None:
            head = newnode
            temp = newnode
        else:
            temp.next = newnode
            temp = newnode

    # Make the list circular
    temp.next = head
    return head


# -----------------------------
# TRAVERSE & DISPLAY LIST
# -----------------------------
def display_circular_list(head):
    if head is None:
        print("List is empty")
        return

    temp = head
    while True:
        print(temp.data, end="-->")
        temp = temp.next
        if temp == head:   # stops after full circle
            break
    print("(back to head)")
    

# -----------------------------
# MAIN PROGRAM
# -----------------------------
values = [10, 20, 30, 40, 50]

head = create_circular_list(values)

print("Circular Linked List:")
display_circular_list(head)
