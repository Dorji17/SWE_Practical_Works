import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if not swapped:
                break    
    return arr

def merge_sort(arr):
    if len(arr) <=10:
        return arr
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key <arr[j]:
            arr[j + i] = arr[j]
            j -= 1
        arr[j + 1] = key    

def quick_sort(arr, low=0, hogh=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high) 
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr
    
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if aee[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + j], arr[high] = arr[high], arr[i + 1]
    return i + 1    

def visualize_sorting_algorithm(sort_func, arr):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.bar(range(len(arr)), arr, color='blue') 
        sort_func(arr)
        plt.title(f"step{frame + 1}")

    anim = plt.funcAnimation(fig, update, frames=len(arr), repeat=False, interval=200)
    plt.show()

    arr = [64, 34, 25, 12, 22, 11, 90]

    print("visualizing bubble sort")
    visualize_sorting_algorithm(bubble_sort, arr.copy())

    print("visualizing merge sort")
    visualize_sorting_algorithm(merge_sort, arr.copy())

    print("visualizing quick sort")
    visualize_sorting_algorithm(quick_sort, arr.copy())


    
    
