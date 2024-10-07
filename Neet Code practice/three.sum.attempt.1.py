# 3 sum bs 

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        triplets = []  # List to store the unique triplets
        
        # Iterate over the array
        for i in range(len(nums) - 2):

            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Need a larger value, move the left pointer
                elif total > 0:
                    right -= 1  # Need a smaller value, move the right pointer
                else:
                    # Found a triplet
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
        
        return triplets
    


solution = Solution()

# Define the test case
nums = [-1,0,1,2,-1,-4]

result = solution.threeSum(nums)
print(f"here are the results {result}")