# Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ----------------------------
# INSERT AT BEGINNING
# ----------------------------
def insert_at_beginning(head, data):
    newnode = Node(data)
    newnode.next = head
    head = newnode
    return head

# ----------------------------
# INSERT AT END
# ----------------------------
def insert_at_end(head, data):
    newnode = Node(data)
    if head is None:
        return newnode
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
    return head

# ----------------------------
# INSERT AT SPECIFIC POSITION
# position starts from 1
# ----------------------------
def insert_at_position(head, data, position):
    newnode = Node(data)

    # Case: inserting at position 1 (beginning)
    if position == 1:
        newnode.next = head
        head = newnode
        return head

    temp = head
    count = 1

    # Traverse to position - 1
    while temp and count < position - 1:
        temp = temp.next
        count += 1

    # If position is out of range
    if temp is None:
        print("Position out of range!")
        return head

    newnode.next = temp.next
    temp.next = newnode
    return head

# ----------------------------
# DISPLAY THE LINKED LIST
# ----------------------------
def display(head):
    temp = head
    while temp:
        print(temp.data, end="-->")
        temp = temp.next
    print("NULL")

# ----------------------------
# MAIN PROGRAM
# ----------------------------

head = None  # start with empty list

# Insert at beginning
head = insert_at_beginning(head, 30)
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head, 10)

print("After inserting at beginning:")
display(head)

# Insert at end
head = insert_at_end(head, 40)
head = insert_at_end(head, 50)

print("\nAfter inserting at end:")
display(head)

# Insert at specific position
head = insert_at_position(head, 25, 3)

print("\nAfter inserting 25 at position 3:")
display(head)
