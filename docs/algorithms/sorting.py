# Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.

# Merge Sort
def merge_sort(arr: []):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) or j < len(right):
            if j == len(right) or (i < len(left) and left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # while i < len(left) and j < len(right):
        #     if left[i] <= right[j]:
        #        The following 4 lines appear 2 times (excluding else)
        #         arr[k] = left[i]
        #         i += 1
        #     else:
        #         arr[k] = right[j]
        #         j += 1
        #     k += 1
        # Repeated while loops could be merged
        # while i < len(left):
        #     arr[k] = left[i]
        #     i += 1
        #     k += 1
        # while j < len(right):
        #     arr[k] = right[j]
        #     j += 1
        #     k += 1


# Code to print the list
def print_list(arr: []):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Bubble Sort
def bubble_sort(arr: []):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

