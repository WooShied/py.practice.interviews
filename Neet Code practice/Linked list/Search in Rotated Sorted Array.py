#Aadil Rashid 10.1.24
# Search in Rotated Sorted Array
# I want to kms

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = 0
        len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if mid is the target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left half
                    right = mid - 1
                else:  # Target is in the right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right half
                    left = mid + 1
                else:  # Target is in the left half
                    right = mid - 1
        
        # If the target is not found, return -1
        return -1