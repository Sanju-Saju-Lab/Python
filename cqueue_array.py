class CQueueArray:
    MAX_SIZE = 10  # Maximum size of the queue

    def __init__(self):
        # Initialize an empty queue with fixed size
        self.queue = [0] * self.MAX_SIZE
        self.front = -1  # Indicates the front of the queue
        self.rear = -1   # Indicates the rear of the queue

    # Enqueue operation: Add an item to the rear of the queue
    def enqueue(self, value):
        # Check if the queue is full (next position is front)
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            print("Queue is full!")
        else:
            # If queue is empty, set front to 0
            if self.front == -1:
                self.front = 0
            # Update rear position and add value to the queue
            self.rear = (self.rear + 1) % self.MAX_SIZE
            self.queue[self.rear] = value
            print(f"{value} enqueued.")

    # Dequeue operation: Remove an item from the front of the queue
    def dequeue(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is empty!")
        else:
            # Print the dequeued value and update front position
            print(f"{self.queue[self.front]} dequeued.")
            # If only one item in the queue, reset the front and rear
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                # Move front to the next item in the circular queue
                self.front = (self.front + 1) % self.MAX_SIZE

    # Peek operation: Show the front item without removing it
    def peek(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is empty!")
        else:
            print(f"Front element is: {self.queue[self.front]}")

    # Display the queue: Show all elements in the queue
    def display(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is empty!")
        else:
            i = self.front
            print("Queue elements:", end=" ")
            # Traverse the queue from front to rear
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.MAX_SIZE
            print(self.queue[self.rear])  # Print the last element

# Main method for user interaction
if __name__ == "__main__":
    # Create a new circular queue object
    cqueue = CQueueArray()
    
    # Infinite loop for user interaction until exit
    while True:
        print("\nChoose an Operation:")
        print("1. Enqueue")  # Add an item to the queue
        print("2. Dequeue")  # Remove an item from the queue
        print("3. Peek")  # View the front item of the queue
        print("4. Display Queue")  # Show all items in the queue
        print("5. Exit")  # Exit the program
        choice = int(input("Enter your choice: "))  # Get user input for operation

        if choice == 1:
            # Ask for a value to enqueue
            value = int(input("Enter value to enqueue: "))
            cqueue.enqueue(value)
        elif choice == 2:
            # Perform dequeue operation
            cqueue.dequeue()
        elif choice == 3:
            # Perform peek operation
            cqueue.peek()
        elif choice == 4:
            # Display the current queue
            cqueue.display()
        elif choice == 5:
            # Exit the program
            print("Exiting...")
            break  # Break out of the loop and terminate
        else:
            print("Invalid choice! Please try again.")  # Invalid choice prompt
