# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Get the pivot index
        quick_sort(arr, low, pi - 1)    # Recursively sort the left part of the array
        quick_sort(arr, pi + 1, high)   # Recursively sort the right part of the array

# Function to partition the array based on the pivot element
def partition(arr, low, high):
    pivot = arr[high]  # The pivot is the last element in the array
    i = low - 1        # The index of the smaller element (initially one before the first element)
    
    # Loop through the array to rearrange elements based on the pivot
    for j in range(low, high):
        if arr[j] < pivot:  # If the current element is smaller than the pivot
            i += 1          # Increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements
    
    # Swap the pivot element with the element at i+1, so pivot is in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the index of the pivot

# Main function to take user input and execute the sorting
def main():
    n = int(input("Enter the number of elements: "))  # Ask for the number of elements
    arr = list(map(int, input("Enter the elements: ").split()))  # Take the elements as input
    
    quick_sort(arr, 0, len(arr) - 1)  # Perform Quick Sort on the entire array

    # Print the sorted array
    print("Sorted Array:")
    print(" ".join(map(str, arr)))  # Convert elements to strings and join with spaces

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
