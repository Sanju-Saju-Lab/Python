# Function to perform merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Split the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the first half
        merge_sort(right_half)  # Recursively sort the second half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to print an array
def print_array(arr):
    print(" ".join(map(str, arr)))

# Main code
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))  # User input for array size
    arr = list(map(int, input("Enter the elements: ").split()))  # User input for array elements

    print("Original Array:")
    print_array(arr)

    merge_sort(arr)  # Perform merge sort

    print("Sorted Array:")
    print_array(arr)
