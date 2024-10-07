#Aadil Rashid 10.1.24
#sort colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # Count occurrences of 0 (red), 1 (white), and 2 (blue)
        counts = [0, 0, 0]

        # Count each color
        for color in nums:
            counts[color] += 1

        # Number of red, white, and blue
        r, w, b = counts

        # Update nums in-place with the sorted order
        nums[:r] = [0] * r  # Fill the first `r` positions with 0s
        nums[r:r + w] = [1] * w  # Fill the next `w` positions with 1s
        nums[r + w:] = [2] * b  # Fill the remaining `b` positions with 2s



