class CQueueArray:
    MAX_SIZE = 10

    def __init__(self):
        self.queue = [0] * self.MAX_SIZE
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, value):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            print("Queue is full!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.MAX_SIZE
            self.queue[self.rear] = value
            print(f"{value} enqueued.")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print(f"{self.queue[self.front]} dequeued.")
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.MAX_SIZE

    # Peek operation
    def peek(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            print(f"Front element is: {self.queue[self.front]}")

    # Display the queue
    def display(self):
        if self.front == -1:
            print("Queue is empty!")
        else:
            i = self.front
            print("Queue elements:", end=" ")
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.MAX_SIZE
            print(self.queue[self.rear])

# Main method for user interaction
if __name__ == "__main__":
    cqueue = CQueueArray()
    while True:
        print("\nChoose an Operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to enqueue: "))
            cqueue.enqueue(value)
        elif choice == 2:
            cqueue.dequeue()
        elif choice == 3:
            cqueue.peek()
        elif choice == 4:
            cqueue.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
