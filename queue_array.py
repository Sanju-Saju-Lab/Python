class QueueArray:
    MAX_SIZE = 10  # Define maximum size of the queue

    def __init__(self):
        self.queue = [None] * self.MAX_SIZE  # Fixed-size array
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        if self.is_full():
            print(f"Queue is full. Cannot add element: {element}")
            return
        self.rear = (self.rear + 1) % self.MAX_SIZE
        self.queue[self.rear] = element
        self.size += 1
        print(f"Enqueued: {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot remove element.")
            return None
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.MAX_SIZE
        self.size -= 1
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.MAX_SIZE

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        for i in range(self.size):
            print(self.queue[(self.front + i) % self.MAX_SIZE], end=" ")
        print()


def main():
    queue = QueueArray()

    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Your choice: "))

        if choice == 1:
            element = int(input("Enter element to enqueue: "))
            queue.enqueue(element)
        elif choice == 2:
            dequeued_element = queue.dequeue()
            if dequeued_element is not None:
                print(f"Dequeued: {dequeued_element}")
        elif choice == 3:
            peek_element = queue.peek()
            if peek_element is not None:
                print(f"Front element: {peek_element}")
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
