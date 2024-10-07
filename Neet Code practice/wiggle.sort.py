#Aadil Rashid 10.6.24
#wiggle sort


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the array
        nums.sort()
        
        n = len(nums)
        
        # Find the middle index (for splitting into two halves)
        mid = (n - 1) // 2
        
        # Create a copy of the sorted array
        sorted_nums = nums[:]
        
        # Fill the wiggle pattern using the index-mapping technique
        j, k = mid, n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = sorted_nums[j]
                j -= 1
            else:
                nums[i] = sorted_nums[k]
                k -= 1
