# merge_sort_chars.py

active_pipes = set()
split_counter = [1]
merge_counter = [1]

def print_merge_state(arr, action):
    parts = []
    for i in range(len(arr)):
        parts.append(str(arr[i]))
        # Insert a pipe after the element if its index is an active division point
        if i in active_pipes:
            parts.append("|")
            
    # Format the string cleanly to remove commas directly before or after pipes
    s = ""
    for item in parts:
        if item == "|":
            s = s.rstrip(", ") + " | "
        else:
            s += item + ", "
    s = s.rstrip(", ")
    
    if action == "Split":
        print(f"Split {split_counter[0]}: {s}")
        split_counter[0] += 1
    elif action == "Merge":
        print(f"Merge {merge_counter[0]}: {s}")
        merge_counter[0] += 1

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        
        # Log the split
        active_pipes.add(mid)
        print_merge_state(arr, "Split")
        
        # Recursively dive left and right
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge the halves
        merge(arr, left, mid, right)
        
        # Remove the division line and log the merge
        active_pipes.remove(mid)
        print_merge_state(arr, "Merge")

def main():
    user_input = input("Enter characters separated by spaces: ")
    arr = user_input.split()
    
    print(f"\nInitial Array: {', '.join(arr)}\n" + "-"*40)
    
    merge_sort(arr, 0, len(arr) - 1)
    
    print("-" * 40 + f"\nFinal Sorted Array: {', '.join(arr)}")

if __name__ == "__main__":
    main()