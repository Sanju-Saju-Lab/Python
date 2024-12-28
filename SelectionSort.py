def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    
    # Loop through the array to sort it
    for i in range(n - 1):
        # Assume the first unsorted element is the smallest
        min_index = i
        
        # Loop through the unsorted part of the array
        for j in range(i + 1, n):
            # If we find a smaller element, update min_index
            if arr[j] < arr[min_index]:
                min_index = j
        
        # If the smallest element is not already in the right place, swap it
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Input: Ask the user for the number of elements
n = int(input("Enter the number of elements: "))
arr = []

# Input: Ask the user to enter the elements
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))  # Append each element to the list

# Call the selection_sort function to sort the array
selection_sort(arr)

# Output: Display the sorted array
print("Sorted array:")
print(arr)
