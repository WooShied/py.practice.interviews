#   Aadil Rashid NeedCode Is Anagram - 8/25/24
#   Explination:
#
#   Length Check: If s and t have different lengths, return False immediately since they cannot be anagrams.
#    Frequency Array: Use a list of size 26 (since there are 26 lowercase English letters) to count character occurrences.
#    Single Pass: In a single loop, you update the count array:
#        For each character in s, increment the corresponding index.
#        For each character in t, decrement the corresponding index.
#    Final Check: After processing, if all counts in the array are zero, the strings are anagrams. Otherwise, they are not.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create a frequency array for 26 lowercase English letters
        count = [0] * 26
        
        # Iterate over both strings simultaneously
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1  # Increment for s
            count[ord(t[i]) - ord('a')] -= 1  # Decrement for t
        
        # Check if all counts are zero
        for c in count:
            if c != 0:
                return False
        
        return True
    


#easy solution using sorted in python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)  