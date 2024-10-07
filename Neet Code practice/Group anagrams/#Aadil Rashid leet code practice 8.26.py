#Aadil Rashid leet code practice 8.26.24 Group anagrams
#Create a Dictionary:

#Use a dictionary (anagrams) where the key is the sorted version of a string, and the value is a list of strings that are anagrams of each other.
#Iterate Over the Input List:

#For each string in the input list:
#Sort the string to get its "canonical form" (i.e., the sorted version).
#Use this sorted string as the key in the dictionary.
#Append the original string to the list corresponding to this key.
#Return the Groups:

#The values of the dictionary will be lists of anagrams. Return these lists.


from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary where each key maps to a list
        anagrams = defaultdict(list)
        
        # Loop over each string in the input list
        for s in strs:
            # Sort the string to find its canonical form
            key = ''.join(sorted(s))
            
            # Add the original string to the list of its anagram group
            anagrams[key].append(s)
        
        # Return all the grouped anagrams as a list of lists
        return list(anagrams.values())
