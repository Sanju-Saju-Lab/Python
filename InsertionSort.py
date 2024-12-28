# Function to perform insertion sort
def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(1, n):  # Start from the second element
        key = arr[i]  # Store the current element to be inserted
        j = i - 1  # Compare with the element before it

        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move to the previous element
        arr[j + 1] = key  # Place the key at its correct position

# Function to print the array
def print_array(arr):
    for num in arr:  # Loop through each element in the array
        print(num, end=" ")  # Print each element with a space
    print()  # Print a new line after printing the array

# Main program
if __name__ == "__main__":
    # Taking the number of elements as input from the user
    n = int(input("Enter the number of elements: "))
    
    # Taking array elements as input from the user
    arr = list(map(int, input("Enter the elements: ").split()))

    # Printing the original array
    print("Original Array:")
    print_array(arr)

    # Perform Insertion Sort
    insertion_sort(arr)

    # Printing the sorted array
    print("Sorted Array:")
    print_array(arr)
