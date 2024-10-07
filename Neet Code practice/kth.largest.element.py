#Aadil Rashid 10.6.24
#Kth Largest Element in an Array
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #creatiing a min heap to get the second largest so we have a time complexity of k
        
        min_heap = nums[:k]
        #heapify transforms a populated list into a heap using heapify func
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]: # Compare with the bottom of the heap
                heapq.heappop(min_heap) #removing the smallest element
                heapq.heappush(min_heap, num)  # Add the new element

        # The root of the min-heap is the kth largest element
        return min_heap[0]

