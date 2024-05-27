def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    arr = [
        [9, 2, 3],
        [4, 5, 6],
        [7, 8, 1]
    ]

    
    flat_arr = [elem for row in arr for elem in row]

    
    quick_sort(flat_arr, 0, len(flat_arr) - 1)

   
    target = int(input("Enter the target element to replace: "))
    replacement = int(input("Enter the replacement element: "))

    
    modified_list = [replacement if x == target else x for x in flat_arr]

    
    modified_arr = [modified_list[i:i + len(arr[0])] for i in range(0, len(modified_list), len(arr[0]))]

    
    print("Modified Array:")
    for row in modified_arr:
        print(row)

if __name__ == "__main__":
    main()
