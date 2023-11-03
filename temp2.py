#Question 2 part a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

def find_pairs_with_sum(arr, target):
    arr = merge_sort(arr)
    for i in arr:
        if binary_search(arr, target - i):
            print(f"Pair found: ({i}, {target - i})")
            
            
#Question 2 part c

import time
import random
import matplotlib.pyplot as plt

def measure_running_time(n):
    S = [random.randint(1, 100) for _ in range(n)]
    target = random.randint(1, 200)
    
    start_time = time.time()
    find_pairs_with_sum(S, target)
    end_time = time.time()
    
    return end_time - start_time

n_values = list(range(1, 10)) + [10, 100, 1000, 10000, 100000, 1000000]
times = []

for n in n_values:
    time_taken = measure_running_time(n)
    times.append(time_taken)

plt.plot(n_values, times)
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Algorithm Scalability')
plt.show()
            


