# Node class for creating a linked list node
class Node:
    def __init__(self, data):
        self.data = data  # Holds the data for the node
        self.next = None  # Points to the next node (initially None)

# SinglyLinkedList class for handling linked list operations
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initially the list is empty, so the head is None

    # Insert a new node at the beginning of the list
    def insert_at_first(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Set the new node as the head of the list

    # Insert a new node at the end of the list
    def insert_at_last(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Insert the new node at the end

    # Insert a new node at a specific position
    def insert_at_position(self, data, pos):
        if pos < 0:  # Validate the position
            print("Position cannot be negative.")
            return

        if pos == 0:  # If position is 0, insert at the beginning
            self.insert_at_first(data)
            return

        new_node = Node(data)  # Create a new node
        current = self.head
        for _ in range(pos - 1):  # Traverse to the node just before the target position
            if current is None:  # If the position exceeds the list size
                print("Position exceeds the list")
                return
            current = current.next

        if current is None:  # Check if the position is still invalid
            print("Position exceeds the list")
            return

        new_node.next = current.next  # Point the new node's next to the current node's next
        current.next = new_node  # Point the current node's next to the new node

    # Remove the first node from the list
    def remove_at_first(self):
        if self.head is None:  # Check if the list is empty
            print("List is empty...")
            return
        print(f"{self.head.data} removed from the list")  # Print the removed node's data
        self.head = self.head.next  # Move the head pointer to the next node

    # Remove the last node from the list
    def remove_at_last(self):
        if self.head is None:  # Check if the list is empty
            print("List is empty...")
            return
        if self.head.next is None:  # If there's only one node, remove it
            self.remove_at_first()
            return

        current = self.head
        while current.next and current.next.next:  # Traverse to the second-to-last node
            current = current.next
        print(f"{current.next.data} removed from the list")  # Print the removed node's data
        current.next = None  # Remove the last node

    # Remove a node from a specific position
    def remove_at_position(self, pos):
        if pos < 0:  # Validate the position
            print("Position cannot be negative.")
            return

        if pos == 0:  # If position is 0, remove the first node
            self.remove_at_first()
            return

        current = self.head
        for _ in range(pos - 1):  # Traverse to the node just before the target position
            if current is None:  # If the position exceeds the list size
                print("Position exceeds list")
                return
            current = current.next

        if current is None or current.next is None:  # Check if the position is invalid
            print("Position exceeds list")
            return

        print(f"{current.next.data} removed from the list")  # Print the removed node's data
        current.next = current.next.next  # Skip over the node to be removed

    # Display the entire linked list
    def display(self):
        current = self.head
        while current:  # Traverse the list
            print(f"{current.data} -> ", end="")  # Print node data
            current = current.next
        print("null")  # Indicate the end of the list

# Main execution
if __name__ == "__main__":
    sll = SinglyLinkedList()  # Create a new linked list
    choice = 1
    # Initial insertion of elements into the list
    while choice == 1:
        data = int(input("Enter data: "))  # Input data for the node
        sll.insert_at_last(data)  # Insert at the end of the list
        choice = int(input("Do you want to insert more elements to the list? 0(No) or 1(Yes): "))

    print("List after initial insertion: ")
    sll.display()  # Display the list after initial insertions

    # Menu for linked list operations
    while True:
        print("\nLinked list operations:")
        print("1. Insert at the beginning.")
        print("2. Insert at the end.")
        print("3. Insert at a specified position.")
        print("4. Remove from the beginning.")
        print("5. Remove from the end.")
        print("6. Remove from a specified position.")
        print("7. Traverse.")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the data: "))
            sll.insert_at_first(data)  # Insert at the beginning
        elif choice == 2:
            data = int(input("Enter the data: "))
            sll.insert_at_last(data)  # Insert at the end
        elif choice == 3:
            data = int(input("Enter the data: "))
            pos = int(input("Enter the position: "))
            sll.insert_at_position(data, pos)  # Insert at a specific position
        elif choice == 4:
            sll.remove_at_first()  # Remove from the beginning
        elif choice == 5:
            sll.remove_at_last()  # Remove from the end
        elif choice == 6:
            pos = int(input("Enter the position: "))
            sll.remove_at_position(pos)  # Remove from a specific position
        elif choice == 7:
            sll.display()  # Display the linked list
        elif choice == 8:
            break  # Exit the loop and end the program
