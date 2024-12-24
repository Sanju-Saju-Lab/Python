class QueueArray:
    MAX_SIZE = 10  # Maximum size of the queue

    def __init__(self):
        self.queue = [None] * self.MAX_SIZE  # Initialize the queue with None values
        self.front = -1  # The front pointer, set to -1 when the queue is empty
        self.rear = -1   # The rear pointer, set to -1 when the queue is empty

    # Adds an element to the queue
    def enqueue(self, element):
        if self.is_full():  # Check if the queue is full
            print(f"Queue is full. Cannot add element: {element}")
            return
        if self.front == -1 and self.rear == -1:  # If the queue is empty
            self.front = 0  # Set front to 0
            self.rear = 0   # Set rear to 0
        else:
            self.rear += 1  # Move rear pointer to the next position
        self.queue[self.rear] = element  # Add the element at the rear position
        print(f"Enqueued: {element}")  # Confirm the addition of the element

    # Removes and returns the front element of the queue
    def dequeue(self):
        if self.is_empty():  # Check if the queue is empty
            print("Queue is empty. Cannot remove element.")
            return -1  # Return -1 if the queue is empty
        element = self.queue[self.front]  # Get the front element
        self.front += 1  # Move the front pointer to the next position
        if self.front > self.rear:  # If the queue becomes empty after the dequeue
            self.front = -1  # Reset front pointer
            self.rear = -1   # Reset rear pointer
        return element  # Return the dequeued element

    # Returns the front element without removing it
    def peek(self):
        if self.is_empty():  # Check if the queue is empty
            print("Queue is empty. Nothing to peek.")
            return -1  # Return -1 if the queue is empty
        return self.queue[self.front]  # Return the front element

    # Checks if the queue is empty
    def is_empty(self):
        return self.front == -1 and self.rear == -1  # True if both front and rear are -1

    # Checks if the queue is full
    def is_full(self):
        return self.rear == self.MAX_SIZE - 1  # True if rear is at the last position of the array

    # Displays all elements in the queue
    def display(self):
        if self.is_empty():  # Check if the queue is empty
            print("Queue is empty.")  # Inform the user if the queue is empty
            return
        print("Queue elements:", end=" ")  # Start displaying elements
        for i in range(self.front, self.rear + 1):  # Loop through elements from front to rear
            print(self.queue[i], end=" ")  # Print each element
        print()  # Print a newline after displaying all elements

# Main function to interact with the user
if __name__ == "__main__":
    queue = QueueArray()  # Create a QueueArray object
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Your choice: "))  # Get user's choice

        if choice == 1:
            element = int(input("Enter element to enqueue: "))  # Get element to enqueue
            queue.enqueue(element)  # Call enqueue method to add element
        elif choice == 2:
            dequeued_element = queue.dequeue()  # Call dequeue method to remove element
            if dequeued_element != -1:  # If the element is successfully dequeued
                print(f"Dequeued: {dequeued_element}")  # Print the dequeued element
        elif choice == 3:
            peeked_element = queue.peek()  # Call peek method to see front element
            if peeked_element != -1:  # If there is an element to peek
                print(f"Front element: {peeked_element}")  # Print the front element
        elif choice == 4:
            queue.display()  # Call display method to show all elements in the queue
        elif choice == 5:
            print("Exiting program. Goodbye!")  # Exit the program
            break  # Break the loop and end the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input
