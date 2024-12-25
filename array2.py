# Define the dimensions of the 2D array
ROWS = 4
COLS = 4

# Initialize a 2D array with all elements set to 0
array = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Function to traverse and display the array
def traverse():
    print("Array elements:")
    for row in array:
        print(" ".join(map(str, row)))  # Display elements of each row

# Function to insert a value into the array at the specified row and column
def insert(row, col, value):
    # Check if the row and column are within valid range
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Invalid index.")
    else:
        array[row][col] = value  # Insert the value at the specified position
        print("Element inserted successfully.")

# Function to delete a value from the array at the specified row and column
def delete(row, col):
    # Check if the row and column are within valid range
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Invalid index.")
    else:
        array[row][col] = 0  # Set the specified position to 0 (delete value)
        print("Element deleted successfully.")

# Function to search for an element by its row and column index
def search_by_index(row, col):
    # Check if the row and column are within valid range
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Invalid index.")
    else:
        print(f"Element at [{row}][{col}]: {array[row][col]}")  # Display element at specified position

# Function to search for a value in the entire array
def search_by_value(value):
    # Loop through the array and search for the specified value
    for i in range(ROWS):
        for j in range(COLS):
            if array[i][j] == value:
                print(f"Value {value} found at index [{i}][{j}].")
                return
    print("Value not found.")  # If value is not found in the array

# Function to update a value in the array at the specified row and column
def update(row, col, value):
    # Check if the row and column are within valid range
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Invalid index.")
    else:
        array[row][col] = value  # Update the value at the specified position
        print("Element updated successfully.")

# Main function to interact with the user
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Insert")
        print("2. Delete")
        print("3. Traverse")
        print("4. Search")
        print("5. Update")
        print("6. Exit")
        choice = int(input("Your Choice: "))  # Get the user's choice
        
        if choice == 1:
            # Ask the user for row, column, and value to insert
            row = int(input(f"Enter row (0-{ROWS-1}): "))
            col = int(input(f"Enter column (0-{COLS-1}): "))
            value = int(input("Enter value to insert: "))
            insert(row, col, value)  # Call the insert function
        elif choice == 2:
            # Ask the user for row and column to delete
            row = int(input(f"Enter row (0-{ROWS-1}): "))
            col = int(input(f"Enter column (0-{COLS-1}): "))
            delete(row, col)  # Call the delete function
        elif choice == 3:
            traverse()  # Display the current array
        elif choice == 4:
            # Ask the user if they want to search by index or value
            search_type = int(input("Enter 1 to search by row and column, 2 by value: "))
            if search_type == 1:
                # Ask for row and column to search
                row = int(input(f"Enter row (0-{ROWS-1}): "))
                col = int(input(f"Enter column (0-{COLS-1}): "))
                search_by_index(row, col)  # Call the search by index function
            elif search_type == 2:
                # Ask for value to search in the array
                value = int(input("Enter value to search: "))
                search_by_value(value)  # Call the search by value function
            else:
                print("Invalid option.")
        elif choice == 5:
            # Ask the user for row, column, and new value to update
            row = int(input(f"Enter row (0-{ROWS-1}): "))
            col = int(input(f"Enter column (0-{COLS-1}): "))
            value = int(input("Enter new value: "))
            update(row, col, value)  # Call the update function
        elif choice == 6:
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Invalid choice handling

# Run the main function when the program starts
if __name__ == "__main__":
    main()
