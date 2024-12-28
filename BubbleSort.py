# Function to perform Bubble Sort on a given list
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    # Outer loop: Repeats passes to move elements to their correct positions
    for i in range(n - 1):
        swapped = False  # Flag to track if any elements were swapped in this pass
        # Inner loop: Compares adjacent elements and swaps them if they are in the wrong order
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the two elements
                swapped = True  # Mark that a swap occurred
        # If no swaps were made, the list is already sorted, so exit the loop early
        if not swapped:
            break

# Taking user input for the number of elements
n = int(input("Enter the number of elements: "))
arr = []  # Initializing an empty list to store the elements
print("Enter the elements: ")
# Reading each element from the user and adding it to the list
for i in range(n):
    arr.append(int(input()))

# Calling the bubble_sort function to sort the list
bubble_sort(arr)

# Displaying the sorted array to the user
print("Sorted array: ")
print(arr)
