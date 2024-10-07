#Aadil Rashid binary search 8/28/24

class Solution:
    def search(self, num: list[int], target: int) -> int:
        low = 0
        high = len(num) - 1

        while low <= high:
            mid = low + (high - low) // 2

            #if target is mid return index
            if num[mid] == target:
                return mid
            
            #if the target is bigger than mid update low 
            elif num[mid] < target: 
                low = mid + 1 
            #if the target is smaller than mid make high equal mid -1
            else: 
                high = mid - 1 
        return -1

