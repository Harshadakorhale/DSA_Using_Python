class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            print(f"Dequeued: {self.queue.pop(0)}")

    # Display operation
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", self.queue)

    def is_empty(self):
        return len(self.queue) == 0


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
