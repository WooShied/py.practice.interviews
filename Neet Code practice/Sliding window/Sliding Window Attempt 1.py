#sliding window Aadil Rashid 8/29/24

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string: convert to lowercase and filter out non-alphanumeric characters
        normalized_str = ''.join(map(str.lower, filter(str.isalnum, s)))
        
        # Initialize pointers
        left, right = 0, len(normalized_str) - 1

        # Check characters from both ends of the string
        while left < right:
            if normalized_str[left] != normalized_str[right]:
                return False  # Characters don't match, so it's not a palindrome
            left += 1  # Move the left pointer to the right
            right -= 1  # Move the right pointer to the left

        return True  # All characters matched, so it is a palindrome
