# Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# -----------------------------
# DELETE FROM BEGINNING
# -----------------------------
def delete_beginning(head):
    if head is None:
        print("List is empty!")
        return None

    head = head.next
    return head


# -----------------------------
# DELETE FROM END
# -----------------------------
def delete_end(head):
    if head is None:
        print("List is empty!")
        return None

    # If only one node
    if head.next is None:
        return None

    temp = head
    while temp.next.next:
        temp = temp.next

    temp.next = None
    return head


# -----------------------------
# DELETE AT SPECIFIC POSITION
# Position starts from 1
# -----------------------------
def delete_at_position(head, position):
    if head is None:
        print("List is empty!")
        return None

    # Delete from position 1
    if position == 1:
        return head.next

    temp = head
    count = 1

    # Traverse to position-1
    while temp and count < position - 1:
        temp = temp.next
        count += 1

    if temp is None or temp.next is None:
        print("Position out of range!")
        return head

    temp.next = temp.next.next
    return head


# -----------------------------
# PRINT LINKED LIST
# -----------------------------
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end="-->")
        temp = temp.next
    print("NULL")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
# Create a sample list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original List:")
print_list(head)

# Delete from beginning
head = delete_beginning(head)
print("\nAfter deleting beginning:")
print_list(head)

# Delete from end
head = delete_end(head)
print("\nAfter deleting end:")
print_list(head)

# Delete at specific position
head = delete_at_position(head, 2)   # delete 2nd node
print("\nAfter deleting node at position 2:")
print_list(head)
