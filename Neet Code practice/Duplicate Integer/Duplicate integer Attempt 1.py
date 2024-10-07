#Duplicate Integer Neet code practice 8/25/24 - Aadil Rashid
#Explanation:

    #seen set: We use a set to keep track of the numbers we have encountered as we iterate through nums.
    #Loop through nums: For each number in nums, we check if it is already in the seen set:
    #    If it is, the method returns True immediately, indicating a duplicate is found.
    #    If it is not, the number is added to the seen set.
    #    Return False: If the loop completes without finding any duplicates, the method returns False.


from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

