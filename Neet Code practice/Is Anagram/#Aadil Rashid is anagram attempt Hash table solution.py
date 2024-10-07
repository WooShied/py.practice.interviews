#Aadil Rashid is anagram attempt
#using hash table
  
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # Add 'self' as the first parameter
        # Check if lengths of s and t are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Counting hash table
        countsrt = {}

        # Counting characters in the first string
        for char in s:
            if char in countsrt:
                countsrt[char] += 1
            else:
                countsrt[char] = 1

        # Decrementing the count based on the second string
        for char in t:
            if char in countsrt:
                countsrt[char] -= 1
                # If any count goes below 0, s and t are not anagrams
                if countsrt[char] < 0:
                    return False
            else:
                # If a character in t is not found in countsrt, s and t are not anagrams
                return False

        # When all counts are zero, s and t are anagrams
        return True
    

# Example usage
solution = Solution()  # Creating an instance of the Solution class
s = "racecar"
t = "carrace"

if solution.isAnagram(s, t):  # Calling the method on the instance
    print(f"'{s}' and '{t}' are anagrams.")
else:
    print(f"'{s}' and '{t}' are not anagrams.")








# 2 hash solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        #counting first string
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        #counting second string
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
    











#one hash solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Create a dictionary to count characters in the first string
        count = {}

        # Count each character in the first string
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Compare counts with the second string
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        # If all values in the dictionary are 0, the strings are anagrams
        return all(value == 0 for value in count.values())

# Example usage
solution = Solution()

s1 = "racecar"
t1 = "carrace"
print(solution.isAnagram(s1, t1))  # Output: True

s2 = "jar"
t2 = "jam"
print(solution.isAnagram(s2, t2))  # Output: False
