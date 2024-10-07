# Aadil Rashid Neet code two intiger sum 8/25/24 
# Explanation:

#    Hash Map (seen): This dictionary stores each number as a key and its index as the value.
#    Iteration:
#        For each number num at index i, calculate the complement that would sum with num to equal the target.
#        If the complement is already in the hash map, return the indices of the complement and the current number.
#        If not, add the current number and its index to the hash map.
#



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


            