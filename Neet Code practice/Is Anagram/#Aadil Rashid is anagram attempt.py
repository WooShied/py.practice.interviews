#Aadil Rashid is anagram attempt
  
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Checks if they are the same len
        if len(s) != len(t):
            return False
        #sort and return true if they are sorted
        return sorted(s) == sorted(t)


solution = Solution()
s = "racecar"
t = "carrace"

if solution.isAnagram(s, t):
    print(f"'{s}' and '{t}' are anagrams.")
else:
    print(f"'{s}' and '{t}' are not anagrams.")

