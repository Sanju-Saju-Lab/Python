class Stack:
    def __init__(self):
        """Initialize the stack with a fixed size."""
        self.MAX_SIZE = 10  # Define the maximum size of the stack
        self.stack = [None] * self.MAX_SIZE  # Create an empty stack with the fixed size
        self.top = -1  # Top points to -1 when the stack is empty

    def push(self, item):
        """Push an item onto the stack."""
        if self.is_full():  # Check if the stack is full
            print(f"Stack Overflow! Can't push {item}")  # Stack overflow error if full
        else:
            self.top += 1  # Move the top pointer up
            self.stack[self.top] = item  # Add the item at the top of the stack
            print(f"Pushed: {item}")  # Inform the user that the item was pushed

    def pop(self):
        """Pop an item from the stack."""
        if self.is_empty():  # Check if the stack is empty
            print("Stack Underflow! Can't pop.")  # Stack underflow error if empty
            return None  # Return None if there is nothing to pop
        else:
            item = self.stack[self.top]  # Get the item from the top of the stack
            self.top -= 1  # Move the top pointer down
            return item  # Return the popped item

    def peek(self):
        """Peek at the top item of the stack."""
        if self.is_empty():  # Check if the stack is empty
            print("Stack is empty!")  # Inform the user if the stack is empty
            return None  # Return None if the stack is empty
        else:
            return self.stack[self.top]  # Return the item at the top of the stack

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1  # Return True if the stack is empty

    def is_full(self):
        """Check if the stack is full."""
        return self.top == self.MAX_SIZE - 1  # Return True if the stack is full

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():  # Check if the stack is empty
            print("Stack is empty!")  # Inform the user if the stack is empty
        else:
            print("Stack:", " ".join(map(str, self.stack[:self.top + 1])))  # Display the stack contents


def main():
    stack = Stack()  # Create an instance of the Stack class with a fixed size

    while True:
        # Display a menu of operations
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))  # Get the user's choice

        if choice == 1:
            value = int(input("Enter the value to push: "))  # Get the value to push
            stack.push(value)  # Push the value onto the stack
        elif choice == 2:
            popped_value = stack.pop()  # Pop a value from the stack
            if popped_value is not None:  # Check if a value was successfully popped
                print(f"Popped: {popped_value}")  # Display the popped value
        elif choice == 3:
            top_value = stack.peek()  # Peek at the top value of the stack
            if top_value is not None:  # Check if there is a top value
                print(f"Top element: {top_value}")  # Display the top value
        elif choice == 4:
            stack.display()  # Display all the items in the stack
        elif choice == 5:
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice! Please try again.")  # Handle invalid input


if __name__ == "__main__":
    main()  # Run the main function to start the program
