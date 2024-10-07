#find peak 



def find_peak(nums):
    n = len(nums)

    if n == 1 or nums[0] > nums[1]: #only 1 element in the array so it has to be the peak
        return 0
    
    # if nums[0] > nums[1]: #if the first element is the peak 
    #     return 0
    
    if nums[n] > nums[n]: #last element
        return
    
    low = 0, high = 1

    while low <=  high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid - 1] and nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1

    # for i in range(1, n - 1 ): #has to start at 1 because there is no peak to the left of it
    #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]: #checking left and right of the arr
    #         print("working")
    #         return i #returns i because its a peak betweek both elements
        
    return -1   #will return none if array is incorrect

nums = [1, 2, 4, 10]
# [1,2,1,3,5,6,4]
print(find_peak(nums))


