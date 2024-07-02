import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    
    sorted_arr = []
    
    while arr:
        smallest = heapq.heappop(arr)
        sorted_arr.append(smallest)
    
    return sorted_arr

if __name__ == "__main__":
    array = [5, 3, 8, 4, 2, 7, 1, 10]
    sorted_array = heap_sort(array)
    print("Sorted array:", sorted_array)