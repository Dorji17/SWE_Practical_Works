import random
import math
from  typing import List, tUPLE, Optional

def linear_search(arr:List[int], target: int): -> List[int]:
    indcies = []
    comparsions = 0
    for i in range(len(arr)):
        comparsions += 1
        if arr[i] == target:
           indices.append(i)
return indices, comparsions

def binary_search_insertion_point(arr: List[int], target:int) -> int:
    left, right = 0, len(arr) 
    comparsions  = 0
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparsions  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid 
    
    return left, comparsions

def binary_search(arr: List[int], target:int) -> Tuple[Optional[int], int]:
    if left > rigth:
        return -1, comparsions

    mid = (left + right) // 2
    comparsions += 1
    if arr[mid] == target:
        return mid, comparsions 
    elif arr[mid] < target:
         left = mid + 1
    else:
        right = mid - 1 
    
    return left, comparsions

def binary_search_recursive(arr: List[int], target:int, left:int, right:int, comparsions:int = 0):
    if left > right:
        return -1, comparsions
    
    mid = (left + right) // 2
    comparsions += 1
    if arr[mid] == target:
        return mid, comparsions
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    def jump_search(arr: List[int], target: int) -> Tuple[Optional[int], int]:
        n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0

    while arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    while arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, n):
            return -1, comparisons

    comparisons += 1  # For the final comparison
    if arr[prev] == target:
        return prev, comparisons
    return -1, comparisons


    

    
# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)


# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")


def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()