MAX_SIZE = 10  # Maximum size of the array
array = [None] * MAX_SIZE  # Array to store elements
size = 0  # Tracks the current number of elements in the array

# Function to display all elements in the array
def traverse():
    print("Array elements:", array[:size])

# Function to insert a new element at a specific index
def insert(index, value):
    global size
    if size >= MAX_SIZE:  # Check if the array is full
        print("Array is full. Cannot insert new element.")
        return
    if index < 0 or index > size:  # Check for a valid index
        print("Invalid index.")
        return
    # Shift elements to the right to make space for the new element
    for i in range(size, index, -1):
        array[i] = array[i - 1]
    array[index] = value  # Insert the new element
    size += 1  # Increase the size of the array
    print("Element inserted successfully.")

# Function to delete an element at a specific index
def delete(index):
    global size
    if index < 0 or index >= size:  # Check for a valid index
        print("Invalid index.")
        return
    # Shift elements to the left to fill the gap
    for i in range(index, size - 1):
        array[i] = array[i + 1]
    size -= 1  # Decrease the size of the array
    print("Element deleted successfully.")

# Function to search for an element by its index
def search_by_index(index):
    if index < 0 or index >= size:  # Check for a valid index
        print("Invalid index.")
        return
    # Display the element at the specified index
    print(f"Element at index {index}: {array[index]}")

# Function to search for an element by its value
def search_by_value(value):
    for i in range(size):
        if array[i] == value:  # Check if the value matches
            print(f"Value {value} found at index {i}.")
            return
    # If the value is not found
    print("Value not found.")

# Function to update an element at a specific index
def update(index, value):
    if index < 0 or index >= size:  # Check for a valid index
        print("Invalid index.")
        return
    array[index] = value  # Update the element
    print("Element updated successfully.")

# Main function to run the program
def main():
    global size
    while True:  # Infinite loop for menu
        print("\nChoose an operation:")
        print("1. Insert")
        print("2. Delete")
        print("3. Traverse")
        print("4. Search")
        print("5. Update")
        print("6. Exit")
        choice = int(input("Your Choice: "))

        if choice == 1:  # Insert operation
            index = int(input(f"Enter index to insert (0-{MAX_SIZE - 1}): "))
            value = int(input("Enter value to insert: "))
            insert(index, value)
        elif choice == 2:  # Delete operation
            index = int(input("Enter index to delete: "))
            delete(index)
        elif choice == 3:  # Traverse operation
            traverse()
        elif choice == 4:  # Search operation
            search_type = int(input("Enter 1 to search by index, 2 by value: "))
            if search_type == 1:
                index = int(input("Enter index to search: "))
                search_by_index(index)
            elif search_type == 2:
                value = int(input("Enter value to search: "))
                search_by_value(value)
            else:
                print("Invalid option.")
        elif choice == 5:  # Update operation
            index = int(input("Enter index to update: "))
            value = int(input("Enter new value: "))
            update(index, value)
        elif choice == 6:  # Exit the program
            print("Exiting program.")
            break
        else:  # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
