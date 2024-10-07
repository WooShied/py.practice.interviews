#the longest consecutive sequence py

# [100, 4, 200, 1, 3, 2] = output: 4
# [0,3,7,2,5,8,4,6,0,1] output: 9

def longest_consecutive_sequence(nums):
    
    if not nums:
        return 0
    
    nums.sort()
    longest_streak = 1
    currrent_streak = 1
    #    0  1  2  3 ....
    # # [1, 2, 3, 4, 5, 8, 100, 200]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]: #checks if current number is different than last   
            if nums[i] == nums[i - 1] + 1: #number is one more than the prev
                currrent_streak += 1
            else:
                longest_streak = max(longest_streak, currrent_streak) #updating the longest streak if current is the longer one
                currrent_streak = 1 #sets current streak back down to 1 
    
    longest_streak = max(longest_streak, currrent_streak)

    return longest_streak


nums = []
print(longest_consecutive_sequence(nums))




def longest_consecutive_sequence_unsorted(nums):
    
    if not nums:
        return 0
    
    nums_set = set(nums)
    longest_streak = 0
    current_streak = 0

    for nums in nums_set:
        
        if nums - 1 not in nums_set:
            current_num = nums
            current_streak = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1

        longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

# nums = [100, 4, 200, 1, 3, 2]
nums = [0,3,7,2,5,8,4,6,0, 1, 10]
print(longest_consecutive_sequence_unsorted(nums))