def minmax(arr, start, end):
    # Base case 1: Only one element in the subarray
    if start == end:
        return arr[start], arr[start]
    
    # Base case 2: Exactly two elements in the subarray
    elif end == start + 1:
        return min(arr[start], arr[end]), max(arr[start], arr[end])
    
    # Recursive case: More than two elements
    else:
        mid = (start + end) // 2
        
        # Recursively find min and max in the left and right halves
        min1, max1 = minmax(arr, start, mid)
        min2, max2 = minmax(arr, mid + 1, end)
        
        # Combine the results
        return min(min1, min2), max(max1, max2)

# Main loop
while True:
    try:
        arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
        
        if len(arr) == 0:
            print("Array cannot be empty. Please enter at least one element.")
            continue
            
        start = 0
        end = len(arr) - 1
        
        # Call the corrected function
        minimum, maximum = minmax(arr, start, end)
        
        print(f"Minimum: {minimum}, Maximum: {maximum}")
        break
        
    except ValueError:
        print("Invalid input. Please enter integers only.")