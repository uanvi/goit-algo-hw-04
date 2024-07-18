import timeit
import random
from tabulate import tabulate

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
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
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def compare_sorting_algorithms():
    datasets = {
        "Small": generate_random_array(100),
        "Medium": generate_random_array(1000),
        "Large": generate_random_array(10000)
    }
    
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Timsort (Python built-in)": sorted
    }
    
    results = []
    
    for dataset_name, dataset in datasets.items():    
        for name, algorithm in algorithms.items():
        
            times = []
            for _ in range(10):  # Run each sorting 10 times for each dataset
                time_taken = timeit.timeit(lambda: algorithm(dataset.copy()), number=1)
                times.append(time_taken)
            
            fastest_time = min(times)
            slowest_time = max(times)
            avg_time = sum(times) / len(times)
            
            results.append([name, dataset_name, f"{fastest_time:.6f} seconds", f"{slowest_time:.6f} seconds", f"{avg_time:.6f} seconds"])
    
    return results

def generate_random_array(size):
    return [random.randint(1, 1000000) for _ in range(size)]

if __name__ == "__main__":
    comparison_results = compare_sorting_algorithms()
    
    # Print results in a table using tabulate
    headers = ["Algorithm", "Dataset Size", "Fastest Time", "Slowest Time", "Average Time"]
    print(tabulate(comparison_results, headers=headers, tablefmt="grid"))
