# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# --------------------------
# TRAVERSAL FUNCTIONS
# --------------------------
def traverse_forward(head):
    temp = head
    last = None
    while temp:
        print(temp.data, end=" <-> ")
        last = temp
        temp = temp.next
    print("NULL")
    return last


def traverse_backward(last):
    temp = last
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.prev
    print("NULL")


# --------------------------
# INSERTION OPERATIONS
# --------------------------
def insert_beginning(head, data):
    newnode = Node(data)
    if head is not None:
        newnode.next = head
        head.prev = newnode
    return newnode


def insert_end(head, data):
    newnode = Node(data)
    if head is None:
        return newnode

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = newnode
    newnode.prev = temp
    return head


def insert_position(head, data, pos):
    newnode = Node(data)

    if pos == 1:
        return insert_beginning(head, data)

    temp = head
    count = 1
    while temp and count < pos - 1:
        temp = temp.next
        count += 1

    if temp is None:
        print("Position out of range!")
        return head

    newnode.next = temp.next
    newnode.prev = temp

    if temp.next:
        temp.next.prev = newnode
    temp.next = newnode

    return head


# --------------------------
# DELETION OPERATIONS
# --------------------------
def delete_beginning(head):
    if head is None:
        print("List empty!")
        return None
    head = head.next
    if head:
        head.prev = None
    return head


def delete_end(head):
    if head is None:
        print("List empty!")
        return None

    if head.next is None:  # Only one node
        return None

    temp = head
    while temp.next:
        temp = temp.next

    temp.prev.next = None
    return head


def delete_position(head, pos):
    if head is None:
        print("List empty!")
        return None

    if pos == 1:
        return delete_beginning(head)

    temp = head
    count = 1

    while temp and count < pos:
        temp = temp.next
        count += 1

    if temp is None:
        print("Position out of range!")
        return head

    if temp.next:
        temp.next.prev = temp.prev
    temp.prev.next = temp.next

    return head


# --------------------------
# MAIN PROGRAM
# --------------------------

head = None

print("=== INSERT AT BEGINNING ===")
head = insert_beginning(head, 30)
head = insert_beginning(head, 20)
head = insert_beginning(head, 10)
last = traverse_forward(head)
print("Backward Traversal: ")
traverse_backward(last)

print("\n=== INSERT AT END ===")
head = insert_end(head, 40)
head = insert_end(head, 50)
last = traverse_forward(head)
print("Backward Traversal: ")
traverse_backward(last)

print("\n=== INSERT AT POSITION (Insert 25 at position 3) ===")
head = insert_position(head, 25, 3)
last = traverse_forward(head)
print("Backward Traversal: ")
traverse_backward(last)

print("\n=== DELETE FROM BEGINNING ===")
head = delete_beginning(head)
last = traverse_forward(head)
print("Backward Traversal: ")
traverse_backward(last)

print("\n=== DELETE FROM END ===")
head = delete_end(head)
last = traverse_forward(head)
print("Backward Traversal: ")
traverse_backward(last)

print("\n=== DELETE FROM POSITION (Delete node at position 3) ===")
head = delete_position(head, 3)
last = traverse_forward(head)
print("Backward Traversal: ")
traverse_backward(last)
