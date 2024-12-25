class DequeArray:
    MAX_SIZE = 10  # Maximum size of the deque

    def __init__(self, size):
        # Initialize the deque with the given size and set front and rear pointers
        self.size = size
        self.deque = [0] * size  # Create an array to hold the deque elements
        self.front = -1  # Front pointer starts at -1 (indicating the deque is empty)
        self.rear = -1   # Rear pointer starts at -1 (indicating the deque is empty)

    def is_empty(self):
        # Check if the deque is empty (when front pointer is -1)
        return self.front == -1

    def is_full(self):
        # Check if the deque is full (when rear is one position before front)
        return (self.rear + 1) % self.size == self.front

    def insert_front(self, value):
        # Insert a value at the front of the deque
        if self.is_full():
            print("Overflow")  # Print overflow message if deque is full
            return
        if self.is_empty():
            # If deque is empty, set both front and rear to 0
            self.front = self.rear = 0
        else:
            # Move front pointer backwards (circularly)
            self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value  # Place the value at the front

    def insert_rear(self, value):
        # Insert a value at the rear of the deque
        if self.is_full():
            print("Overflow")  # Print overflow message if deque is full
            return
        if self.is_empty():
            # If deque is empty, set both front and rear to 0
            self.front = self.rear = 0
        else:
            # Move rear pointer forward (circularly)
            self.rear = (self.rear + 1) % self.size
        self.deque[self.rear] = value  # Place the value at the rear

    def delete_front(self):
        # Delete the element from the front of the deque
        if self.is_empty():
            print("Underflow")  # Print underflow message if deque is empty
            return
        if self.front == self.rear:
            # If only one element is left, reset both front and rear to -1
            self.front = self.rear = -1
        else:
            # Move front pointer forward (circularly)
            self.front = (self.front + 1) % self.size

    def delete_rear(self):
        # Delete the element from the rear of the deque
        if self.is_empty():
            print("Underflow")  # Print underflow message if deque is empty
            return
        if self.front == self.rear:
            # If only one element is left, reset both front and rear to -1
            self.front = self.rear = -1
        else:
            # Move rear pointer backwards (circularly)
            self.rear = (self.rear - 1 + self.size) % self.size

    def display(self):
        # Display the elements of the deque
        if self.is_empty():
            print("Deque is empty")  # If deque is empty, print a message
            return
        i = self.front
        print("Deque:", end=" ")
        while True:
            print(self.deque[i], end=" ")  # Print the current element
            if i == self.rear:
                break  # Stop when the rear is reached
            i = (i + 1) % self.size  # Move to the next element circularly
        print()  # Move to the next line after printing all elements

def main():
    MAX_SIZE = 10
    deque = DequeArray(MAX_SIZE)  # Create a deque object with a maximum size

    deque_type = 0
    while deque_type not in [1, 2]:
        print("Choose deque type:")
        print("1. Input Restricted")
        print("2. Output Restricted")
        deque_type = int(input("Your choice: "))  # User input for deque type
    
    while True:
        print("\nChoose an operation:")
        if deque_type == 1:  # Input Restricted
            print("1. Insert at Rear")
            print("2. Delete from Front")
            print("3. Delete from Rear")
        else:  # Output Restricted
            print("1. Insert at Front")
            print("2. Insert at Rear")
            print("3. Delete from Front")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Your choice: "))  # User input for operation choice

        if choice == 5:
            break  # Exit the loop if user chooses 5

        if choice == 1:
            value = int(input("Enter value: "))  # User input for value
            if deque_type == 1:
                deque.insert_rear(value)  # Insert at rear for input restricted deque
            else:
                deque.insert_front(value)  # Insert at front for output restricted deque
        elif choice == 2:
            if deque_type == 1:
                deque.delete_front()  # Delete from front for input restricted deque
            else:
                value = int(input("Enter value: "))
                deque.insert_rear(value)  # Insert at rear for output restricted deque
        elif choice == 3:
            if deque_type == 1:
                deque.delete_rear()  # Delete from rear for input restricted deque
            else:
                deque.delete_front()  # Delete from front for output restricted deque
        elif choice == 4:
            deque.display()  # Display the current elements in the deque
        else:
            print("Invalid choice")  # Handle invalid user input

if __name__ == "__main__":
    main()  # Run the main function
