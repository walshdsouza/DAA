# quick_sort_numbers.py

step_quick = [1]

def print_quick_state(arr, low, high):
    parts = []
    # Loop one extra time to catch trailing empty arrays
    for i in range(len(arr) + 1):
        # Handle empty sub-array base cases
        if i == low and low > high:
            parts.append("[]")
        
        if i < len(arr):
            # Format the active bounds and the pivot
            if i == low and low <= high:
                if low == high: # Size 1 base case
                    parts.append(f"[**{arr[i]}**]")
                else:           # Start of larger partition
                    parts.append(f"[**{arr[i]}**")
            elif i == high and low < high:
                parts.append(f"{arr[i]}]")
            else:
                parts.append(str(arr[i]))
                
    # Join parts to a string
    s = ", ".join(parts)
    print(f"Iteration {step_quick[0]}: {s}")
    step_quick[0] += 1

def partition(arr, low, high):
    pivot = arr[low]
    store_index = low + 1
    
    for i in range(low + 1, high + 1):
        if arr[i] > pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
            
    arr[low], arr[store_index - 1] = arr[store_index - 1], arr[low]
    return store_index - 1

def quick_sort(arr, low, high):
    # Print state before doing any logic
    print_quick_state(arr, low, high)
    
    # Base cases: array of size 1 or empty
    if low >= high:
        return
        
    # Execute the partition and lock the pivot
    pi = partition(arr, low, high)
    
    # Dive left and right of the locked pivot
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)

def main():
    user_input = input("Enter numbers separated by spaces: ")
    
    try:
        arr = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please ensure you only enter numbers.")
        return
        
    print("\n" + "-"*40)
    
    quick_sort(arr, 0, len(arr) - 1)
    
    print("-" * 40 + f"\nFinal Sorted Array: {arr}")

if __name__ == "__main__":
    main()