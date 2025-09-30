import heapq 

heap = [3,1,2]
heapq.heapify(heap) # Convert list to heap
heapq.heappush(heap, 0) # Add element to heap
print(heap) # Output: [0, 1, 2, 3] (0 is the smallest)
print(heapq.heappop(heap)) # Remove and return the smallest element (0)
print(heap) # Output: [1, 3, 2] (0 is removed)