class Stack:
    def __init__(self, size):
        """Initialize the stack with a fixed size."""
        self.stack = [None] * size
        self.top = -1
        self.capacity = size

    def push(self, item):
        """Push an item onto the stack."""
        if self.is_full():
            print(f"Stack Overflow! Can't push {item}")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"Pushed: {item}")

    def pop(self):
        """Pop an item from the stack."""
        if self.is_empty():
            print("Stack Underflow! Can't pop.")
            return None
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

    def peek(self):
        """Peek at the top item of the stack."""
        if self.is_empty():
            print("Stack is empty!")
            return None
        else:
            return self.stack[self.top]

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1

    def is_full(self):
        """Check if the stack is full."""
        return self.top == self.capacity - 1

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack:", " ".join(map(str, self.stack[:self.top + 1])))


def main():
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)

    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to push: "))
            stack.push(value)
        elif choice == 2:
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped: {popped_value}")
        elif choice == 3:
            top_value = stack.peek()
            if top_value is not None:
                print(f"Top element: {top_value}")
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
