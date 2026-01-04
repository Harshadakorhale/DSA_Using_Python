class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued: {data}")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
            return
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued: {removed}")

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        temp = self.front
        print("Queue elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Creating a queue
q = Queue()

# Performing operations
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()
q.display()

q.dequeue()
q.dequeue()
q.dequeue()  
