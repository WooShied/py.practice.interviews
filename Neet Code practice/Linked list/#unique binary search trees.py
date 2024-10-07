#unique binary search trees
# Aadil Rashid 10.4.24

class Solution:
    def numTrees(self, n: int) -> int:
        
        # Dictionary to store already computed results
        seen = {}

        # Helper function to calculate the number of unique BSTs in the range [start, end]
        def helper(start, end):
            # Base case: If the range is invalid or only one node is left, return 1 (a valid tree)
            if start < 1 or end > n or start >= end:
                return 1
            
            # Check if the result for this range has already been calculated
            if (start, end) in seen:
                return seen[(start, end)]  # Return the cached result if found
            
            # Variable to store the count of unique BSTs for this range
            count = 0
            
            # Iterate through each number in the range [start, end] as a potential root
            for i in range(start, end + 1):
                # Recursively count the unique BSTs formed by the left subtree (numbers less than i)
                left_subtrees = helper(start, i - 1)
                # Recursively count the unique BSTs formed by the right subtree (numbers greater than i)
                right_subtrees = helper(i + 1, end)
                # Multiply the count of left and right subtrees and add to the total count
                count += left_subtrees * right_subtrees

            # Store the computed result in the dictionary for future use
            seen[(start, end)] = count
            return count  # Return the count of unique BSTs for this range
        
        # Start the recursion for the full range [1, n]
        return helper(1, n)
