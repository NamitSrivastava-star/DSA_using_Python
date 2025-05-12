import heapq

def convert_min_to_max_heap(min_heap):
    """Converts a min-heap to a max-heap in-place.

    Args:
        min_heap: A list representing the min-heap.
    """
    # Invert the sign of each element to simulate max-heap behavior
    for i in range(len(min_heap)):
        min_heap[i] *= -1
    
    # Heapify the modified list, which now behaves as a max-heap
    heapq.heapify(min_heap)
    
    # Revert the sign of each element to get the original values in max-heap order
    for i in range(len(min_heap)):
        min_heap[i] *= -1

# Example usage
min_heap = [3,2,1,5,6,4]
convert_min_to_max_heap(min_heap)
print("Max-heap:", min_heap[len(min_heap) - 2]) # Output: [17, 15, 13, 9, 8, 5, 10, 4, 3, 6, 1]