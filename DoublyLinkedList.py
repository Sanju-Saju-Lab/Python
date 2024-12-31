# Node class represents a node in the doubly linked list.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

# DLL class represents the doubly linked list itself.
class DLL:
    def __init__(self):
        self.head = None  # The first node in the list
        self.tail = None  # The last node in the list

    # Method to append a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Make the new node both the head and the tail
            self.tail = new_node
            return
        # If the list is not empty, add the node at the end
        new_node.prev = self.tail  # Set the previous pointer of new node
        self.tail.next = new_node  # Set the next pointer of the old tail
        self.tail = new_node  # Update the tail to the new node

    # Method to prepend a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
            return
        # If the list is not empty, add the node at the start
        self.head.prev = new_node  # Set the previous pointer of the old head
        new_node.next = self.head  # Set the next pointer of the new node
        self.head = new_node  # Update the head to the new node

    # Method to insert a node at a specific position
    def insert_at_position(self, pos, data):
        new_node = Node(data)  # Create a new node
        if pos == 1:  # If inserting at the beginning
            self.prepend(data)
            return
        current = self.head  # Start from the head of the list
        current_position = 1  # Track the current position in the list
        while current and current_position < pos - 1:  # Traverse to the desired position
            current = current.next
            current_position += 1
        if not current:  # If position is invalid
            print("Invalid position.")
        elif current == self.tail:  # If the position is at the end, append the node
            self.append(data)
        else:
            # Insert the new node between two existing nodes
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    # Method to delete the first node
    def delete_first(self):
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        if self.head == self.tail:  # If the list has only one node
            self.head = self.tail = None
        else:
            # If there are multiple nodes, update the head
            self.head = self.head.next
            self.head.prev = None

    # Method to delete the last node
    def delete_last(self):
        if self.tail is None:  # If the list is empty
            print("List is empty.")
            return
        if self.head == self.tail:  # If the list has only one node
            self.head = self.tail = None
        else:
            # If there are multiple nodes, update the tail
            self.tail = self.tail.prev
            self.tail.next = None

    # Method to delete a node at a specific position
    def delete_node(self, pos):
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        if pos == 1:  # If deleting the first node
            self.delete_first()
            return
        current = self.head  # Start from the head of the list
        current_position = 1
        while current and current_position < pos:  # Traverse to the desired position
            current = current.next
            current_position += 1
        if not current:  # If position is invalid
            print("Invalid position.")
        elif current == self.tail:  # If deleting the last node
            self.delete_last()
        else:
            # Update the pointers to exclude the current node
            current.prev.next = current.next
            current.next.prev = current.prev

    # Method to traverse the list in the forward direction and print the nodes
    def traverse_forward(self):
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        current = self.head
        while current:  # Traverse the list from head to tail
            print(current.data, end=" ")
            current = current.next
        print()

    # Method to traverse the list in the backward direction and print the nodes
    def traverse_backward(self):
        if self.tail is None:  # If the list is empty
            print("List is empty.")
            return
        current = self.tail
        while current:  # Traverse the list from tail to head
            print(current.data, end=" ")
            current = current.prev
        print()

# Main function to interact with the user
if __name__ == "__main__":
    dll = DLL()  # Create a new doubly linked list
    choice = 1
    while choice == 1:
        data = int(input("Enter the data: "))  # Get data from user
        dll.append(data)  # Append data to the list
        choice = int(input("Do you want to insert more elements? 0(No) or 1(Yes): "))
    
    dll.traverse_forward()  # Print the list after initial entries

    while True:
        # Display menu to the user
        print("\nDoubly Linked List Menu")
        print("1. Insert at the beginning.")
        print("2. Insert at the end.")
        print("3. Insert at a specified position.")
        print("4. Remove from the beginning.")
        print("5. Remove from the end.")
        print("6. Remove from a specified position.")
        print("7. Traverse Forward")
        print("8. Traverse Backward")
        print("9. Exit")
        menu_choice = int(input("Enter your choice: "))

        # Handle user input for various operations
        if menu_choice == 1:
            data = int(input("Enter the data: "))
            dll.prepend(data)
            dll.traverse_forward()
        elif menu_choice == 2:
            data = int(input("Enter the data: "))
            dll.append(data)
            dll.traverse_forward()
        elif menu_choice == 3:
            data = int(input("Enter the data: "))
            position = int(input("Enter the position: "))
            dll.insert_at_position(position, data)
            dll.traverse_forward()
        elif menu_choice == 4:
            dll.delete_first()
            dll.traverse_forward()
        elif menu_choice == 5:
            dll.delete_last()
            dll.traverse_forward()
        elif menu_choice == 6:
            pos = int(input("Enter the position: "))
            dll.delete_node(pos)
            dll.traverse_forward()
        elif menu_choice == 7:
            print("Traverse Forward:")
            dll.traverse_forward()
        elif menu_choice == 8:
            print("Traverse Backward:")
            dll.traverse_backward()
        elif menu_choice == 9:
            print("Exited")
            break
        else:
            print("Invalid choice. Please try again.")
